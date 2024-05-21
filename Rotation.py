import cv2
import math

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w / 2, h / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image, rotation_matrix

def rotate_bboxes(bboxes, rotation_matrix, img_size):
    new_bboxes = []
    h, w = img_size

    for bbox in bboxes:
        cls_id, x_center, y_center, bbox_width, bbox_height = bbox
        x_center = x_center * w
        y_center = y_center * h
        bbox_width = bbox_width * w
        bbox_height = bbox_height * h

        corners = [
            (x_center - bbox_width / 2, y_center - bbox_height / 2),
            (x_center + bbox_width / 2, y_center - bbox_height / 2),
            (x_center - bbox_width / 2, y_center + bbox_height / 2),
            (x_center + bbox_width / 2, y_center + bbox_height / 2)
        ]

        new_corners = []
        for corner in corners:
            new_x = rotation_matrix[0, 0] * corner[0] + rotation_matrix[0, 1] * corner[1] + rotation_matrix[0, 2]
            new_y = rotation_matrix[1, 0] * corner[0] + rotation_matrix[1, 1] * corner[1] + rotation_matrix[1, 2]
            new_corners.append((new_x, new_y))

        new_x_center = (new_corners[0][0] + new_corners[3][0]) / 2 / w
        new_y_center = (new_corners[0][1] + new_corners[3][1]) / 2 / h
        new_bbox_width = abs(new_corners[0][0] - new_corners[3][0]) / w
        new_bbox_height = abs(new_corners[0][1] - new_corners[3][1]) / h

        new_bboxes.append([cls_id, new_x_center, new_y_center, new_bbox_width, new_bbox_height])

    return new_bboxes

# Example usage
if __name__ == '__main__':
    image_path = "your_image_path_here.jpg"
    annotation_path = "your_annotation_path_here.txt"
    output_image_path = "your_output_image_path_here.jpg"
    output_annotation_path = "your_output_annotation_path_here.txt"

    image = cv2.imread(image_path)
    with open(annotation_path) as f:
        bboxes = [list(map(float, line.strip().split())) for line in f.readlines()]

    angle = 45  # Rotation angle in degrees
    rotated_image, rotation_matrix = rotate_image(image, angle)
    new_bboxes = rotate_bboxes(bboxes, rotation_matrix, image.shape[:2])
    cv2.imwrite(output_image_path, rotated_image)
    save_yolo_format(new_bboxes, output_annotation_path)

    print(f"Saved rotated image to {output_image_path} and annotations to {output_annotation_path}")

