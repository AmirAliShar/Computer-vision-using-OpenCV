import cv2

# Initialize webcam (0 = default camera)
cap = cv2.VideoCapture(0) 

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

# Get frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#To save as MP4 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height)) #20.0 Frames per second
print("Recording... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Write frame to file
    out.write(frame)

    # Show the frame
    cv2.imshow('Webcam Recording', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved as output.avi")