#!/usr/bin/env python
import rospy
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import Image as Img
from PIL import Image
from datetime import datetime

frame = 0
size = (2048, 1536) # 
frameRate = 15.0 # 
now = datetime.now()
fileName = "output/" + now.strftime("%d_%m_%Y-%H_%M_%S")
fourcc = cv.VideoWriter_fourcc(*'MJPG')
vid = cv.VideoWriter(fileName + ".avi", fourcc, frameRate, size, True)

def visualRecorder(data):
    global frame
    if(vid.isOpened() and frame < (int(sys.argv[2]) * int(frameRate))):
        bridge = CvBridge()
        img = bridge.imgmsg_to_cv2(data)
        img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
        vid.write(img)
        frame += 1
    else:
        print("Video recorder turned off. Outputting file.")
        vid.release()
        sys.exit()


def listener():
    inter = 0
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("[TOPIC]", Img, visualRecorder)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
