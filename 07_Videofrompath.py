import cv2

# Load saved video file
video_path = "OpenCV/vid.mp4"   # or "output.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

print("Playing video... Press 'q' to exit")

while True:
    ret, frame = cap.read()

    # If video ends
    if not ret:
        print("End of video")
        break

    # Show the video frame
    cv2.imshow("Saved Video", frame)

    # Press 'q' to exit early
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()