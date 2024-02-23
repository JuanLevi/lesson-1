import cv2

image1=cv2.imread('openCV.png',1)

cv2.imshow('OpenCV',image1)
cv2.waitKey(2000)
#cv2.imwrite("opencvGrey.png",image1)
print(image1.shape)

B,G,R=cv2.split(image1)

cv2.imshow('Blue',B)
cv2.waitKey(2000)
cv2.imshow('Green',G)
cv2.waitKey(2000)
cv2.imshow('Red',R)
cv2.waitKey(2000)

image2=cv2.imread('pikachu.png',1)
print(image2.shape)
h,w=image2.shape[0:2]
ROI=image2[0:300,100:200]
cv2.imshow('ROI',ROI)
cv2.waitKey(3000)
