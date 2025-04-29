import cv2 as cv
import numpy as np   
import math
img = cv.imread("img1.jpg", cv.IMREAD_GRAYSCALE) #link to input picture
#img = cv.imread("contrast.png", cv.IMREAD_GRAYSCALE)



def logtransformfunc(img, index):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype = np.uint8)
    
    for i in range(height):
        for j in range(width):
            singlepixel = img[i, j]
            newpixel = index * math.log(1 + singlepixel)
            matrixzeros[i, j] = newpixel
    return matrixzeros


def logtransformfunc2(img, r1, r2):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype = np.uint8)
    for i in range(height):
        for j in range(width):
            singlepixel = img[i, j]
            if singlepixel < r1:
                newpixel = 0
            elif singlepixel > r2:
                newpixel = 255
            else:
                newpixel = (singlepixel - r1) * (255 / (r2 - r1))
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
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            singlepixel = img[i,j]
            newpixel = index * (singlepixel ** (1/index))
            matrixzeros[i, j] = newpixel
    return matrixzeros


def logtransformfunc4(img, min_val, max_val, c):
    height, width = img.shape[:2]
    matrixzeros = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            singlepixel = img[i, j]
            if singlepixel < min_val:
                matrixzeros[i, j] = singlepixel  
            elif singlepixel > max_val:
                matrixzeros[i, j] = singlepixel  
            else:             
                normalized = (singlepixel - min_val) / (max_val - min_val)  
                newpixel = c * math.log(1 + normalized) * (max_val - min_val) + min_val
                matrixzeros[i, j] = np.clip(newpixel, 0, 255)
    
    return matrixzeros

newimglog = logtransformfunc(img, 90)
newimgThreshold = thresholdfunc(img, 127)
newimgIdentity = indentityfunc(img)
newimgnegative = negativefunc(img)
newimgpower = powerfunc(img, 4)
newimgroot = rootfunc(img, 2)
newimglog2 = logtransformfunc2(img, 100, 200)
newimglog3 = cv.cvtColor(newimglog2, cv.COLOR_GRAY2RGB)
newimglog4 = logtransformfunc4(img, 50, 100, -10)



cv.imshow("Original img", img)
# cv.imshow("after log transform", newimglog)
# cv.imshow("after threshold", newimgThreshold)
# cv.imshow("after identity", newimgIdentity)
# cv.imshow ("after negative", newimgnegative)
# cv.imshow("after power", newimgpower)
# cv.imshow("after root", newimgroot)
# cv.imshow("after log2", newimglog2)
# cv.imshow("after log3", newimglog3)
cv.imshow("after log4", newimglog4)





cv.waitKey(0)