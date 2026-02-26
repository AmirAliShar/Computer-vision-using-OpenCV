# H , W , channel
import cv2
import matplotlib.pyplot as plt

image =cv2.imread("OpenCV/rose.jpeg")

if image is not None:
#     cv2.imshow(image)
    w,h,c =image.shape
    #print(f"Imagae\n Height: {h} \n Weight: {w}\n Channel: {c}")

gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(10, 10))

# Display Original Image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

# Display Gray Image
plt.subplot(1, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Gray Image")
plt.axis('off')

plt.show()