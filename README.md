# Autonomous Indoor Navigation of Quadcopter

The objective of this project is to predict the path in which the quadcopter should move in avoiding obstacles in its path in a GPS denied environment using a camera only, without any external sensors.The quadcopter is of the DJI-F450 frame and the flight controller used is Pixhawk 2.4.8.

# Setup
You would need the following dependencies installed in your computer before cloning this repository:

1. Python 3.6 (This is a must. In other versions you may experience trouble.)
2. TensorFlow (The GPU version if you have a GPU)
3. OpenCV 3.4.2 (This also is a must.)

The use of Anaconda is advised since it is easier to install and remove dependencies as you please.

# Training
Semantic Segmentation model DeepLabV3 was trained for object detection and pixel labelling. We have used the CamVid dataset for training the model. The training tesults are as follows:

<img src="https://user-images.githubusercontent.com/49706145/57769542-cb52a180-772b-11e9-8883-f901f8c040ab.png" width="50%" height="50%">
<img src="https://user-images.githubusercontent.com/49706145/57769559-d4dc0980-772b-11e9-8d22-0d1dba1367d1.png" width="50%" height="50%">
<img src="https://user-images.githubusercontent.com/49706145/57769560-d574a000-772b-11e9-95d0-5d9d4a716124.png" width="50%" height="50%">

You can change most parsing variables in the code with almost the same result.

If you want your own prediction data, you can use your phone camera and set the resolution at 960x720 since the training was done for this resolution.

Though the dataset is meant for road traffic navigation, the trained model gives suprisingly good results for an indoor environment. You can choose your environment to take a picture and try it out.

# Path Prediction
For the angle determination and path prediction, we have developed our own algorithm based on OpenCV. After semantic segmentation, this algorithm predicts the angle in wich the quadcopter may travel, and the distance it may travel in that direction. 
Currently, the model is able to predict a straight line path with an angle prediction for left-right (yaw) angular rotation. 
Examples of path prediction:

<img src="https://user-images.githubusercontent.com/49706145/57771523-8ed57480-7730-11e9-9ece-8b6c2579f2aa.png" width="50%" height="50%">
<img src="https://user-images.githubusercontent.com/49706145/57771345-11116900-7730-11e9-8ab5-acad15cb5ade.png" width="50%" height="50%">

The project can be further extended to other rotational angles of the UAV, i.e., pitch and roll.

# Acknowledgements
Most codes have been cloned from the GitHub repository GeorgeSeif/Semantic-Segmentation-Suite: https://github.com/GeorgeSeif/Semantic-Segmentation-Suite
