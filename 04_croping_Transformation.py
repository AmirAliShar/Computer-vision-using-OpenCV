import cv2

# croped = image[starty:endy, startx, endx]

img= cv2.imread("OpenCV/rose.jpeg")

if img is not None:
    croped =img[50:100,100:200]
    cv2.imshow("Image",img)
    cv2.imshow("Croped Image", croped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()