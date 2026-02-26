import cv2

image = cv2.imread("OpenCV/amir.jpg")

#Image Rotation
if image is not None:
    print("Image Loaded")

    (h,w)=image.shape[:2]

    center =(h//2, w//2)

    M =cv2.getRotationMatrix2D(center,45,1)

    rotated =cv2.warpAffine(image, M,(w,h))

    cv2.imshow("Orginal Image ",image)
    cv2.imshow("Rotated ",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if image is None:
    print("Image is not loaded")
else:
    print("Image Loade")
    # Flipping
    #cv2.flip(src,flip) (0--> TOB, 1--> LTR, -1 --> Both)
    vertical =cv2.flip(image,0)
    hori =cv2.flip(image,1)
    both =cv2.flip(image,-1)
    cv2.imshow("vertical ",vertical)
    cv2.imshow("Horizontal ",hori)
    cv2.imshow("Both ",both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()