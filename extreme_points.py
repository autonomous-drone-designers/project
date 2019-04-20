# USAGE
# python extreme_points.py

# import the necessary packages
import imutils
import cv2
from PIL import Image
import numpy as np
import math


def distance(x1, y1,x2,y2):
    dist = math.sqrt((math.fabs(x2-x1))**2+((math.fabs(y2-y1)))**2)
    return dist

# load the image, convert it to grayscale, and blur it slightly
img = cv2.imread("img2.png")
print('Original Dimensions : ',img.shape)
 
scale_percent = 25 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

#cv2.imshow("Resized image", resized)
#im = Image.open("img1.png")
#pix = im.load()
#cv2.imshow("image",im)
val=np.array([128, 64, 128])
mask = cv2.inRange(resized, val, val)
res = cv2.bitwise_and(resized,resized, mask= mask)
"""
cv2.imshow('frame',resized)
cv2.imshow('mask',mask)
cv2.imshow('res',res)"""
#im.show()
#print(im.size)  # Get the width and hight of the image for iterating over
#print(pix[613,300])
#print(im.getcolors(maxcolors=256))
val=np.array([128, 64, 128])
#print(val)


"""# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)"""

# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
#extLeft = tuple(c[c[:, :, 0].argmin()][0])
#extRight = tuple(c[c[:, :, 0].argmax()][0])
orangex,orangey = tuple(c[c[:, :, 1].argmin()][0])
print(orangex,orangey)
#extBot = tuple(c[c[:, :, 1].argmax()][0])

hypotenuse =  distance(orangex,orangey, int(width/2), height-20)
vertical=distance(int(width/2),height-20,int(width/2),orangey)
angle1=np.arccos((vertical/hypotenuse))*180/math.pi
if orangex<=int(width/2):
    angle1=-angle1
    print(int(angle1))
cv2.line(resized, (orangex, orangey), (int(width/2),height-20), (0, 0, 255), 2)
cv2.line(resized, (int(width/2),height-20), (int(width/2),orangey), (0, 0, 255), 2)
cv2.putText(resized, str(int(angle1)), (int(width/2)+5,height-35 ), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.75, (255,255,255), 1)
extTop= (orangex,orangey)
# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
cv2.drawContours(resized, [c], -1, (0, 255, 255), 2)
#cv2.circle(resized, extLeft, 6, (0, 0, 255), -1)
#cv2.circle(resized, extRight, 6, (0, 255, 0), -1)
cv2.circle(resized, extTop, 6, (255, 0, 0), -1)
#cv2.circle(resized, extBot, 6, (255, 255, 0), -1)

# show the output image
cv2.imshow("Image", resized)
cv2.waitKey(0)
