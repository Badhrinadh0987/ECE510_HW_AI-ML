
import dlib
import cv2
import numpy as np
import os

predictor_path = "shape_predictor_68_face_landmarks.dat"
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(predictor_path)

def extract_eye_mouth_features_from_frame(frame):
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

def capture_dataset():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access webcam.")
        return

    os.makedirs("dataset/features", exist_ok=True)
    os.makedirs("dataset/labels", exist_ok=True)

    count = 0
    print("Instructions:")
    print(" - Press A to label frame as ALERT")
    print(" - Press D to label frame as DROWSY")
    print(" - Press ESC to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        display = frame.copy()
        cv2.putText(display, f"Sample #{count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Capture - Press A/D/ESC", display)
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break
        elif key in [ord('a'), ord('d')]:
            label = 0 if key == ord('a') else 1
            features = extract_eye_mouth_features_from_frame(frame)
            if features is not None:
                np.save(f"dataset/features/sample_{count}.npy", features)
                with open(f"dataset/labels/sample_{count}.txt", "w") as f:
                    f.write(str(label))
                print(f"Saved sample #{count} with label {label}")
                count += 1
            else:
                print("No face detected. Try again.")

    cap.release()
    cv2.destroyAllWindows()
    print(f"Finished. Collected {count} samples.")

if __name__ == "__main__":
    capture_dataset()
