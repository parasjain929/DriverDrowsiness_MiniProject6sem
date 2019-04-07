# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:18:06 2019

@author: Parar Jain
"""
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
imprt dlib
import cv2

def sound_alarm(path):
    playsound.playsound(path)
    
def eye_aspect_ratio(eye):

    A=dist.euclidean(eye[1], eye[5])
    B=dist.euclidean(eye[2], eye[4])

    C=dist.euclidean(eye[0, eye[3]])    
    
    ear =(A+B)/(2.0 * C)
    
    return ear

ap=argparse.ArgumentParser()
ap.add_argument("-p","--shape-predictor",required=True,)

