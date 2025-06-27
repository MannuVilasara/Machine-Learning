import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Press 's' to Save image", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        cv2.imwrite("saved_image.png", frame)
        print("Image saved as 'saved_image.png'")
        cv2.imshow("Saved Image", frame)
    elif key == ord("q"):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
