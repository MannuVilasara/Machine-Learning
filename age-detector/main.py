import cv2
import numpy as np

AGE_MODEL = "age_net.caffemodel"
AGE_PROTO = "age_deploy.prototxt"

AGE_RANGES = ["0-2", "4-6", "8-12", "15-20", "25-32", "38-43", "48-53", "60-100"]

age_net = cv2.dnn.readNetFromCaffe(AGE_PROTO, AGE_MODEL)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        face = frame[y : y + h, x : x + w]
        blob = cv2.dnn.blobFromImage(
            face,
            1.0,
            (227, 227),
            (78.4263377603, 87.7689143744, 114.895847746),
            swapRB=False,
        )
        age_net.setInput(blob)
        age_preds = age_net.forward()
        age = AGE_RANGES[age_preds[0].argmax()]

        label = f"Age: {age}"
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
            frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
        )

    cv2.imshow("Age Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
