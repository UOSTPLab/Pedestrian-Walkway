# Import the YOLO class from the ultralytics library
from ultralytics import YOLO  

# Load a pretrained YOLOv8 model from a specific path
model_path = '/best.pt'  # The path to your trained model
model = YOLO(model_path)  # Create a YOLO object using the specified model

# Run inference on an image and obtain a list of results
results = model('.jpg')  # Provide the path to the image you want to analyze

# Define the names of fixed obstacles for classification
fixed_obstacles_names = ['tree', 'light', 'sign', 'fireplug']  # List of fixed obstacle names

# Initialize a dictionary to classify and store detected objects into fixed and non-fixed categories
classified_obstacles = {'fixed': [], 'non_fixed': []}

# Iterate over each detection result
for r in results:
    print(r.boxes)  # Print the Boxes object containing the detection bounding boxes
    # Classify each detected object based on its class name
    for box in r.boxes:
        cls_name = model.names[int(box.cls)]  # Extract the class name using the class ID
        # Check if the class name is in the list of fixed obstacles
        if cls_name in fixed_obstacles_names:
            classified_obstacles['fixed'].append(cls_name)  # Add to fixed obstacles if true
        else:
            classified_obstacles['non_fixed'].append(cls_name)  # Otherwise, add to non-fixed obstacles

# Print the classified results
print(classified_obstacles)
