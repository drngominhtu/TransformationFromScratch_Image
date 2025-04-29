#contrast stretching 
#biến đổi ảnh tăng độ tương phản dark > K < light
#điểm ảnh tối > K < điểm ảnh sáng
#if (dark < k) then dark --
#if (light > k) then light ++

#thresholding 
#biến đổi nhị phân
#dark = 0 (min); light = 1 (max) if {dark < K} else 1
#dark = 1 (max); light = 0 (min) if {dark > K} else 0


#bài toán tìm ngưỡng k cho ảnh đầu vào

#some intentity transform functions
# indentity s = r -> biến đổi nhưng không thay đổi gì ->> không thay đổi gì
# negative: s = -r + 255 -> đảo ngược màu sắc ->> đảo ngược màu sắc
# log: s = c * log(1 + r) -> tăng độ tương phản cho ảnh tối ->> tập trung dải giá trị L/4 đến L - 1 trở thành 3L/4 đến L - 1
# gamma: s = c * r^gamma -> tăng độ tương phản cho ảnh sáng ->>    
# power: s = c * r^gamma -> tăng độ tương phản cho ảnh sáng ->>
# inverse log: s = c * exp(r) -> tăng độ tương phản cho ảnh sáng
# inverse gamma: s = c * r^(1/gamma) -> tăng độ tương phản cho ảnh sáng
# root: s = c * r^(1/gamma) -> tăng độ tương phản cho ảnh sáng
# histogram equalization/streching: s = c * r^(1/gamma) -> tăng độ tương phản cho ảnh sáng




import cv2 as cv
import numpy as np
import math

img = cv.imread("img1.jpg", cv.IMREAD_GRAYSCALE)

def logTransform(img, c):
    height, width = img.shape[:2]
    result = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            pixel = img[i,j]
            newpixel = c * math.log(1 + pixel)
            result[i, j] = np.clip(newpixel, 0, 255)
    return result


if img is None:
    print("fail to read")
else:
    print("read successful")
    newimg = logTransform(img, 40)
    cv.imshow("Original img", img)
    cv.imshow("after log transform", newimg)


