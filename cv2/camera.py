import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
    	continue
   
    mirror = cv2.flip(img, 1)
    cv2.imshow("camera", mirror)
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()
