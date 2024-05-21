import cv2
import random
import os

def random_crop(image, bboxes, output_size):
    h, w, _ = image.shape
    new_h, new_w = output_size

    if new_h > h or new_w > w:
        raise ValueError("Crop size should be smaller than the original size")

    top = random.randint(0, h - new_h)
    left = random.randint(0, w - new_w)

    cropped_image = image[top: top + new_h, left: left + new_w]

    new_bboxes = []
    for bbox in bboxes:
        cls_id, x_center, y_center, bbox_width, bbox_height = bbox
        x_center = x_center * w
        y_center = y_center * h
        bbox_width = bbox_width * w
        bbox_height = bbox_height * h

        x_min = x_center - bbox_width / 2
        y_min = y_center - bbox_height / 2
        x_max = x_center + bbox_width / 2
        y_max = y_center + bbox_height / 2

        x_min = max(0, x_min - left)
        y_min = max(0, y_min - top)
        x_max = min(new_w, x_max - left)
        y_max = min(new_h, y_max - top)

        if x_min >= x_max or y_min >= y_max:
            continue

        new_x_center = (x_min + x_max) / 2 / new_w
        new_y_center = (y_min + y_max) / 2 / new_h
        new_bbox_width = (x_max - x_min) / new_w
        new_bbox_height = (y_max - y_min) / new_h

        new_bboxes.append([cls_id, new_x_center, new_y_center, new_bbox_width, new_bbox_height])

    return cropped_image, new_bboxes

def save_yolo_format(bboxes, output_path):
    with open(output_path, 'w') as f:
        for bbox in bboxes:
            f.write(" ".join(map(str, bbox)) + '\n')

# Example usage
if __name__ == '__main__':
    image_path = "your_image_path_here.jpg"
    annotation_path = "your_annotation_path_here.txt"
    output_image_path = "your_output_image_path_here.jpg"
    output_annotation_path = "your_output_annotation_path_here.txt"

    image = cv2.imread(image_path)
    with open(annotation_path) as f:
        bboxes = [list(map(float, line.strip().split())) for line in f.readlines()]

    cropped_image, new_bboxes = random_crop(image, bboxes, output_size=(300, 300))
    cv2.imwrite(output_image_path, cropped_image)
    save_yolo_format(new_bboxes, output_annotation_path)

    print(f"Saved cropped image to {output_image_path} and annotations to {output_annotation_path}")
