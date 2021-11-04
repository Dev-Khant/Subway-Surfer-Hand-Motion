# Subway Surfers with Hand Motions

![image](https://user-images.githubusercontent.com/57898986/139538138-b3455166-59ec-4d5a-b52c-3c8adb3f7391.png)


## Object Detection Model

Built an Object Detector which detects the position of Hand and accordingly predicts the movement. The movements are Up, Down, Right, Left. These movements are then passed to the game.<br><br>

Model used for detection is SSD_MobileNet_V2_FPNLite from Tensorflow Object Detection API [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) and for setting up the environment go through the official article [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/). Folder for Tensorflow Object Detection API is on MASTER branch .<br><br>

Used custom dataset consisting of 250 train images and 50 test images for each class.





