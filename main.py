from __future__ import print_function
import cv2
import math
import random

capture = cv2.VideoCapture(0)
if not capture.isOpened:
    print('Unable to open camera')
    exit(0)

sectorsX = 2
sectorsY = 2

while True:
    ret, frame = capture.read()
    
    if frame is None:
        print("No frame, is the camera connected?")
        break

    height, width, channels = frame.shape

    out = frame
    sectorWidth = math.floor(width / sectorsX)
    sectorHeight = math.floor(height / sectorsY)
    
    for y in range(sectorsX):
        for x in range(sectorsY):
            sectorFrame = out[y*sectorHeight:(y+1)*sectorHeight, x*sectorWidth:(x+1)*sectorWidth]
            cv2.imshow('Display ' + str(y) + ':' + str(x), sectorFrame)
    

    key = cv2.waitKey(1)
    keyAscii = chr(key & 255)
        
    if keyAscii == 'q' or key == 27:
        break
