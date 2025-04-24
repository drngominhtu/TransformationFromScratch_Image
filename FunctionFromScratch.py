import cv2 as cv
import numpy as np   
import math
img = cv.imread("img1.jpg", cv.IMREAD_GRAYSCALE) #link to input picture

def logtransformfunc(img, index):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype = np.uint8)
    

    for i in range(height):
        for j in range(width):
            singlepixel = img[i, j]
            newpixel = index * math.log(1 + singlepixel)
            matrixzeros[i, j] = newpixel
    return matrixzeros


def thresholdfunc(img, index):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype = np.uint8)
    
    for i in range(height):
        for j in range(width):
            singlepixel = img[i, j]
            if singlepixel > index:
                matrixzeros[i, j] = 255
            else:
                matrixzeros[i, j] = 0
    return matrixzeros



def indentityfunc(img):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype = np.uint8)
    for i in range (height):
        for j in range (width):
            singlepixel = img[i, j]
            newpixel = singlepixel
            matrixzeros[i, j] = newpixel
    return matrixzeros            


def negativefunc(img):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype= np.uint8)
    for i in range(height):
        for j in range(width):
            singlepixel = img[i, j]
            newpixel = 255 - singlepixel
            matrixzeros[i, j] = newpixel
    return matrixzeros
cv.imshow("Original img", img)


def powerfunc(img, index):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype=np.uint8)
    for i in range (height):
        for j in range(width):
            singlepixel = img[i, j]
            newpixel = index * (singlepixel ** index)
            matrixzeros[i,j] = newpixel
    return matrixzeros


def rootfunc(img, index):
    height, width = img.shpae[:2]
    matrixzeros = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            singlepixel = img[i,j]
            newpixel = index * (singlepixel ** (1/index))
            matrixzeros[i, j] = newpixel
    return matrixzeros


newimglog = logtransformfunc(img, 90)
newimgThreshold = thresholdfunc(img, 127)
newimgIdentity = indentityfunc(img)
newimgnegative = negativefunc(img)
newimgpower = powerfunc(img, 4)
newimgroot = rootfunc(img, 2)


cv.imshow("after log transform", newimglog)
cv.imshow("after threshold", newimgThreshold)
cv.imshow("after identity", newimgIdentity)
cv.imshow ("after negative", newimgnegative)
cv.imshow("after power", newimgpower)
cv.imshow("after root", newimgroot)
cv.waitKey(0)