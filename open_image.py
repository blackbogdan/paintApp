import cv2
import numpy as np

# image = cv2.imread('birds.jpg')
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(image[0][0])
# print(len(image[0][0]))
# # print(image.size/3)
# print(image.shape)


# print('='*59, "GRAY")
# h, w = grey.shape
# print(grey.shape)
# print(type(grey))
# print(grey.size)
# print(h, w)
# print(grey)
# cv2.imshow("image", image)
# cv2.imshow("image", grey)
# cv2.waitKey()


# zeros_array = np.zeros(2352, dtype=int)
# zeros_array = zeros_array.reshape(-1, 3)
# zeros_array.astype(np.uint8)
# print(zeros_array)
# gray = cv2.cvtColor(zeros_array, cv2.COLOR_RGB2GRAY)
# print(gray.size)
img = np.zeros([5,5,3])

# img[:,:,0] = np.ones([5,5])*255/255.0
img[:,:,2] = np.ones([5,5])*255/255.0
# img[:,:,1] = np.ones([5,5])*128/255.0
# img[:,:,2] = np.ones([5,5])*192/255.0
print(img)

cv2.imshow("image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
cv2.waitKey()
cv2.INTER_LINEAR