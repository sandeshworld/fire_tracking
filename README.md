# fire_tracking
detecting fire and pointing gimbal towards it

This project has two parts. The first part was doing a test run using a simple gimbal. This was functioning. I utilized OPENCV HSV filter and blob detection, then utilized the detection coordinate in the frame, ran it through a gimbal control node that ran a PID that tried to keep the object at the
center of the frame. This worked really well. For now, I implemented it for one axis but adding
the second one is simple as declaring a second set of classes in the code.

TO RUN BASIC ONE FOR ADAFRUIT SERVO ARM TO DETECT BLACK OBJECT:
1. make sure to have uploaded the arduino ros code into the teensy 3.2
2. roslaunch gimbal_control gimbal_control.launch
3. run rviz and then show the images from blob_detector and etc.
