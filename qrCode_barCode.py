import cv2
import numpy as np
from pyzbar.pyzbar import decode

#for image
#img = cv2.imread('qrcodeimage1.jpg')
# code = decode(img)   #prints all the information like rect , data, type 
# print(code)

#for webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
     ret, img = cap.read()
     for barcode in decode(img):
        print(barcode.data)     #prints only the data
        myData = barcode.data.decode('utf-8')
        print(myData)
     cv2.imshow('result',img)
     cv2.waitKey(0)