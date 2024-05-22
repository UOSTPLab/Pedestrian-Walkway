# Pedestrian-Walkway

The codebase consists of five components:

1. RandomCropping
2. Rotation
3. Fixed and non-fixed obstacle detection
4. VOC2YOLO
5. YOLO2VOC

Explanations for each code component are provided in the comments.


# Introduction
We have identified sections with the highest pedestrian traffic in each of the 25 districts across Seoul and collected data on obstacles in the pedestrian walkways.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/3c052e71-4acb-431a-ab2e-e678649528cd)

Furthermore, we designed specific guidelines for data collection to ensure uniform conditions during capture. This design ensured that different surveyors captured images under the same conditions, maintaining the consistency of the dataset.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/c5e7cf79-3b73-4001-8b90-2d4b4cc1d9f1)

The dataset comprises a total of 9 classes: car, garbage bin, break, advertisement, fire hydrant, streetlight, personal mobility device, motorcycle, and tree.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/5f5e9155-08dc-41c1-9d63-3de3b35cf09e)

The images include (a) a car, (b) a garbage bin , (c) a broken walkway surface, (d) an advertisement , (e) a fire hydrant, (f) a streetlight in the walkway, (g) a personal mobility (h) a motorcycle and tree

Data augmentation techniques were applied to simulate various weather conditions on the pedestrian walkways.
To reflect weather and other environmental conditions, we used data augmentation techniques from Automold--Road-Augmentation-Library(https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library). Additionally, to prevent overfitting, we applied Random Cropping and Rotation for data augmentation. The codes for these augmentations can be found in the files 1. RandomCropping.py and 2. Rotation.py.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/21c0872c-92c8-465e-8051-3158c73f5b65)

To reflect real-time events occurring on pedestrian walkways, the collected images were classified into two groups: fixed obstacles and non-fixed obstacles. Fixed obstacles, such as trees, streetlights, and signs, are essential components of the walkways and cannot be removed or improved. In contrast, non-fixed obstacles, like motorcycles and personal mobility devices, are temporary and can be improved as they arise from transient events. This distinction underscores the diverse characteristics and predictable behavior patterns of the obstacles, making it crucial to provide a detailed classification for each class.
The code to automatically classify fixed and non-fixed obstacles can be found in the file named 3. Fixed and non-fixed obstacle detection.py.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/5c5f05da-e3f0-4e39-8f4e-14f948071aab)


# Dataset Utilization Strategies

By utilizing this dataset, one can develop models for pedestrian walkway obstacle detection and classification based on the degree of damage. This approach can assess the pedestrian environment, reduce maintenance costs for walkways, and improve the walking environment. Additionally, it can aid in establishing efficient path planning for autonomous delivery robots and other robots that navigate pedestrian walkways in the future.
![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/0e4e0b01-75c4-4636-8647-18ccc5b65a81)

Additionally, to ensure the interpretability of the detected objects, we applied Explainable Artificial Intelligence (XAI) techniques. Specifically, we used Grad-CAM from the pytorch-grad-cam library(https://github.com/jacobgil/pytorch-grad-cam). XXAI provides transparency by highlighting which parts of the objects the model considers important for detection, thereby enhancing the reliability of the model's decision-making process.
![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/2f911582-1516-4b4a-ac2f-6ec18e785c6e)

