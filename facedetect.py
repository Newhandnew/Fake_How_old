import numpy as np
import cv2
import random

def facedetect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #face pattern

    img = cv2.imread('test.jpg')        #read test.png
    #cv2.imshow('original', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #change color from BGR to Gray

    font = cv2.FONT_HERSHEY_SIMPLEX     # detect font

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)     #face scale range 1.3
    #draw rectangle and random number
    for (x,y,w,h) in faces:     
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,100,200),2)
        cv2.putText(img, str(random.randrange(15, 25)), (x+(w/2)-20, y-10), font, 1,(255,255,255),2,cv2.LINE_AA)
    #cv2.imshow('result image',img)
    #cv2.waitKey(0)
    cv2.imwrite("./result.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) #save as result.png with compression parameter
    #cv2.destroyAllWindows()
    return 0

