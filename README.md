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

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/10512d8d-c3a9-4b15-b6c6-d3149bba6fa5)


Furthermore, we designed specific guidelines for data collection to ensure uniform conditions during capture. These standardized procedures are crucial for maintaining data consistency and ensuring homogeneity during the subsequent data preprocessing and analysis stages.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/fd1fafa1-b64e-4c15-9d86-67697a4e152c)

The dataset consists of a total of 9 classes.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/2fb7ff19-e606-4740-8a0f-5b616e96c47f)

The images include (a) a parked car on the pedestrian walkway, (b) a garbage bin obstructing paths, (c) a broken and uneven walkway surface, (d) an advertising board encroaching on pedestrian space, (e) a fire hydrant blocking part of the walkway, (f) a streetlight post positioned in the walkway, (g) a personal mobility device along with its accompanying sign, and (h) a motorcycle parked on the sidewalk. Each example highlights common issues that pedestrians encounter on the walkways.

Data augmentation techniques were applied to simulate various weather conditions on the pedestrian walkways.
To reflect weather and other environmental conditions, we used data augmentation techniques from Automold--Road-Augmentation-Library(https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library). Additionally, to prevent overfitting, we applied Random Cropping and Rotation for data augmentation. The codes for these augmentations can be found in the files 1. RandomCropping.py and 2. Rotation.py.

![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/21c0872c-92c8-465e-8051-3158c73f5b65)

For deep learning purposes, the collected images were divided into four types of fixed obstacles and six types of non-fixed obstacles. The fixed obstacles, such as trees, streetlights, and signs, are essential components of the pedestrian walkways. They pose necessary components, and obstructions that cannot be removed or improved. In contrast, the non-fixed obstacles, such as motorcycles, PMs, and breaks, occur temporarily, presenting obstructions that can be improved. This differentiation implies that the nature and predictable behavior patterns of the objects vary, making it crucial to provide a detailed and specific classification for each class. The model plays a key role in understanding various scenarios and in enabling more precise predictions.
The code to automatically classify fixed and non-fixed obstacles can be found in the file named 3. Fixed and non-fixed obstacle detection.py.

# Dataset Utilization Strategies

By utilizing this dataset, one can develop models for pedestrian walkway obstacle detection and classification based on the degree of damage. This approach can assess the pedestrian environment, reduce maintenance costs for walkways, and improve the walking environment. Additionally, it can aid in establishing efficient path planning for autonomous delivery robots and other robots that navigate pedestrian walkways in the future.
![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/0e4e0b01-75c4-4636-8647-18ccc5b65a81)

Additionally, to ensure the interpretability of the detected objects, we applied Explainable Artificial Intelligence (XAI) techniques. Specifically, we used Grad-CAM from the pytorch-grad-cam library(https://github.com/jacobgil/pytorch-grad-cam). XAI provides transparency by highlighting which parts of the objects the model considers important for detection, thereby offering reliability and trustworthiness in the model's decision-making process.
![image](https://github.com/UOSTPLab/Pedestrian-Walkway/assets/166711870/2f911582-1516-4b4a-ac2f-6ec18e785c6e)

