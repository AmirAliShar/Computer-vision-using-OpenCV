import cv2

VidCap= cv2.VideoCapture(0)

while True:
    ret, frame = VidCap.read() #ret = false/true and frame = iamge

    if not ret :
        print("Could not read frame:")
        break
    cv2.imshow("Webcam feed",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Quiting....")
        break
VidCap.release()
cv2.destroyAllWindows()