import cv2
import imageio

# RTMP stream URL
rtmp_url = "rtmp://192.168.43.157:1935/live"

# Create a VideoCapture object using imageio
cap = imageio.get_reader(f'rtmp://192.168.43.157:1935/live', 'ffmpeg')

# Create a window to display the stream
cv2.namedWindow("RTMP Stream", cv2.WINDOW_NORMAL)

for frame in cap:
    # Display the frame
    cv2.imshow("RTMP Stream", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the window
cv2.destroyAllWindows()
