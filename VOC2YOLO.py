import xml.etree.ElementTree as ET
import os

# Function to convert VOC XML file to YOLO format
def voc_to_yolo(xml_file, output_dir, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    filename = root.find('filename').text
    txt_filename = os.path.splitext(filename)[0] + '.txt'
    txt_path = os.path.join(output_dir, txt_filename)

    with open(txt_path, 'w') as f:
        for obj in root.findall('object'):
            difficult = obj.find('difficult').text
            if int(difficult) == 1:
                continue

            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)

            xmlbox = obj.find('bndbox')
            xmin = float(xmlbox.find('xmin').text)
            xmax = float(xmlbox.find('xmax').text)
            ymin = float(xmlbox.find('ymin').text)
            ymax = float(xmlbox.find('ymax').text)

            # Calculate YOLO format values
            x_center = (xmin + xmax) / 2.0 / width
            y_center = (ymin + ymax) / 2.0 / height
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height

            f.write(f"{cls_id} {x_center} {y_center} {w} {h}\n")

# Main script execution
if __name__ == '__main__':
    # Define the classes
    classes = ["tree", "light", "sign", "fireplug", "adver", "bin", "motorcycle", "PM", "car", "break"]
    
    # Define the paths
    xml_file = "your_voc_xml_path_here.xml"  # Path to the provided XML file
    output_dir = "your_output_directory_here"  # Directory where YOLO format files will be saved
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert the provided XML file
    voc_to_yolo(xml_file, output_dir, classes)
    
    print(f"Converted {xml_file} to YOLO format and saved in {output_dir}")
