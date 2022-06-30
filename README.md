# QT_ROS_Recording
## Installation Instructions
1. On your QT2 (not tested for QT1) make sure you are in the QTPC (if you can see a desktop screen then you are in the right place)
2. Open a terminal and run "cd catkin_ws/src/"
3. Clone this repo by clicking the "Code" button on this website and copying the link, then run "git clone \[link\]" 

## Running Instructions
1. Make sure you are in the root of this directory on your QTPC, that means you should be in `catkin_ws/src/QT_ROS_Recording`
2. Run "python scripts/listener.py -r" 
3. The QT is now recording. To finish, hit `ctrl+c` on the keyboard
4. The output video will be in .avi format and will be named today's date. It will be inside the "output" folder