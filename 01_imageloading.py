import cv2

#Show the image
# img = cv2.imread("OpenCV/rose.jpeg")
# if img is not None:
#     cv2.imshow("Window Title", img) #open the window
#     cv2.waitKey(0) #wait for user to press any key
#     cv2.destroyAllWindows()
# else:
#     print("Please give the correct path")

# Save the image

image =cv2.imread('OpenCV/amir.jpg')
if image is not None:
    succ =cv2.imwrite("image_write.jpeg",image)
    if succ:
        print("save successfully")
    else:
        print("did not save.")
else:
    print("Image is not read")