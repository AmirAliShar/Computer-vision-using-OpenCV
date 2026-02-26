# Resizing the image

# res =cv2.resize(src, fx,fy, interpolation)
import cv2 
img =cv2.imread("OpenCV/rose.jpeg")

if img is None:
    print("Image is not Found")
else:
    
    res_img = cv2.resize(img,(300,300))

    cv2.imshow("Orginal Image", img)
    cv2.imshow("Resized image ", res_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#     plt.subplot(1,2,1)
#     plt.imshow(img)
#     plt.title("Orginal Image")
#     plt.axis('off')

#     plt.subplot(1,2,2)
#     plt.imshow(res_img)
#     plt.title("Resized Image")
#     plt.axis('off')
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

