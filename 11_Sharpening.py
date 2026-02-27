#Highlight the edges and details in image
import cv2
import  numpy as np
import matplotlib.pyplot as plt
# (src,ddepth,kernel)

img =cv2.imread("OpenCV/amir.jpg")

#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # Not Need because save the RGB image
BLClean=cv2.bilateralFilter(img,3,10,10)
GSClean=cv2.GaussianBlur(img,(3,3),3)
MedianClean=cv2.medianBlur(img,3)

# Sharpening kernel
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])
sharpen=cv2.filter2D(img,-1,kernel)


# Show results
titles = ["Original", "Gaussian Blur", "Median Blur", "Bilateral Filter","sharpen"]
images = [img, GSClean, MedianClean,BLClean,sharpen]


plt.figure(figsize=(18,18))
for i in range(5):
    plt.subplot(1,7,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()