import cv2

print("The camera is turn on\nfor exit enter q and for take photo enter s")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("error to open")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("error to read frame")
        break
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('photo.jpg', frame)
        print("عکس گرفته شد و ذخیره شد.")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
