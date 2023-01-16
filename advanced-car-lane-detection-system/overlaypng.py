import cv2
import numpy as np
import cvzone

imgBack = cv2.imread('highways.png')
imgFront = cv2.imread('1.png', cv2.IMREAD_UNCHANGED)
imgFront2 = cv2.imread('2.png', cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture('project_video.mp4')
while True:

    success, img = cap.read()
    #img = cvzone.overlayPNG(img, imgFront2, [630, 620])
    img = cvzone.overlayPNG(img, imgFront, [630, 580])
    img = cvzone.overlayPNG(img, imgFront2, [630, 540])
    
    img = cv2.putText(img, 'y', (0, 234), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))

    

    cv2.imshow('image', img)
    #cv2.imshow('image', img)
    cv2.waitKey(1)