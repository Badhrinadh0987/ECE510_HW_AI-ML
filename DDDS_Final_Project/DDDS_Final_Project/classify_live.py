
import dlib
import cv2
import numpy as np
import joblib

predictor_path = "shape_predictor_68_face_landmarks.dat"
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(predictor_path)
model_path = "model/drowsiness_classifier.pkl"

def extract_eye_mouth_features(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray, 1)
    if len(faces) == 0:
        return None

    shape = landmark_predictor(gray, faces[0])
    coords = np.zeros((68, 2), dtype="float")
    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    selected = np.concatenate((coords[36:48], coords[48:68]), axis=0)
    return selected.flatten()

def live_classification():
    model = joblib.load(model_path)
    cap = cv2.VideoCapture(0)

    print("🔁 Press ESC to exit")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        features = extract_eye_mouth_features(frame)
        label = None

        if features is not None:
            prediction = model.predict([features])[0]
            proba = model.predict_proba([features])[0][prediction]
            label = "DROWSY" if prediction == 1 else "ALERT"
            cv2.putText(frame, f"{label} ({proba:.2f})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255) if label == "DROWSY" else (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No face detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)

        cv2.imshow("Live Drowsiness Detection", frame)
        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_classification()
