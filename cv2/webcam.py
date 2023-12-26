import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
    	continue
    
    height, width, _ = img.shape

    center_x = width // 2
    center_y = height // 2
    
    x1 = width // 4
    x2 = x1 * 3
    y1 = height // 4
    y2 = y1 * 3

    img = cv2.line(img, (0, center_y), (width, center_y), (255, 255, 255), 2)

    img = cv2.line(img, (center_x, 0), (center_x, height), (255, 255, 255), 2)
    
    img = cv2.line(img, (x1, y1), (x2, y1), (255, 255, 255), 2)
    img = cv2.line(img, (x1, y2), (x1, y1), (255, 255, 255), 2)
    img = cv2.line(img, (x2, y1), (x2, y2), (255, 255, 255), 2)
    img = cv2.line(img, (x2, y2), (x1, y2), (255, 255, 255), 2)
    
    mirror = cv2.flip(img, 1)
    cv2.putText(mirror, "Kyialbek", (x1, height//8 * 7), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("camera", mirror)
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()
