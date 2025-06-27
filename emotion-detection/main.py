import cv2
from deepface import DeepFace

# Load the face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=6, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        face = frame[y : y + h, x : x + w]
        try:
            result = DeepFace.analyze(
                face, actions=["emotion"], enforce_detection=False
            )
            emotion = result[0]["dominant_emotion"]
        except Exception as e:
            emotion = "Error"
            print(f"Error analyzing face: {e}")

        # Draw rectangle and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            str(emotion),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (36, 255, 12),
            2,
        )

    # Show the video
    cv2.imshow("Emotion Detection", frame)

    # Break the loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
