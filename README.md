# Subway Surfers with Hand Motions

![img](https://user-images.githubusercontent.com/57898986/140607483-332a70eb-05ba-44d3-b1e7-b6d3a9036597.png)


## Object Detection Model

Built an Object Detector which detects the position of Hand and accordingly predicts the movement. The movements are Up, Down, Right, Left. These movements are then passed to the game.<br><br>

Model used for detection is SSD_MobileNet_V2_FPNLite as it can detect object in around 25ms with the help of Tensorflow Object Detection API [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) and for setting up the environment go through the official article [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/).<br> 
Folder for Tensorflow Object Detection API is on MASTER branch .<br><br>

Used custom dataset consisting of 250 train images and 50 test images for each class.<br><br>

The link for the working video [YouTube](https://www.youtube.com/watch?v=LYiCKA1DeFg).





