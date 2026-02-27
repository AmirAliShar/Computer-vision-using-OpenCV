import cv2

#Gassian = cv2.GaussianBlur(image,(kernelSize_X,kernelSize_Y),gamma) #Average of the pixels
img =cv2.imread("OpenCV/amir.jpg")

gausian = cv2.GaussianBlur(img,(5,5),3)

cv2.imshow("Orginal Image ", img)
cv2.imshow("Gaussian Blurred ", gausian)

#MedianBlur --> It take median value of pixels and apply the blur
median = cv2.medianBlur(img,9)
cv2.imshow("Medain Blured ", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
