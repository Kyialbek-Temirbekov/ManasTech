import cv2

# RTMP stream URL
rtmp_url = "rtmp://192.168.0.102:1935/live"

# Create a VideoCapture object
cap = cv2.VideoCapture(rtmp_url)

# Check if the video capture is successful
if not cap.isOpened():
    print("Error: Could not open the RTMP stream.")
    exit()

# Create a window to display the stream
cv2.namedWindow("RTMP Stream", cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the RTMP stream
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Failed to read frame from the RTMP stream.")
        continue

    # Display the frame
    cv2.imshow("RTMP Stream", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the window
cap.release()
cv2.destroyAllWindows()

