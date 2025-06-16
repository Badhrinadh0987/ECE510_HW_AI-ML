
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
        print("No face detected.")
        return None

    shape = landmark_predictor(gray, faces[0])
    coords = np.zeros((68, 2), dtype="float")
    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    # Extract eyes (36–47) and mouth (48–67)
    selected = np.concatenate((coords[36:48], coords[48:68]), axis=0)
    flat_features = selected.flatten()

    return flat_features

def capture_from_webcam_and_extract():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Webcam not accessible.")
        return

    print("Press SPACE to capture an image.")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow("Press SPACE to capture", frame)
        key = cv2.waitKey(1)
        if key == 32:  # SPACE key
            features = extract_eye_mouth_features_from_frame(frame)
            if features is not None:
                os.makedirs("reduced_dataset", exist_ok=True)
                np.save("reduced_dataset/eye_mouth_features.npy", features)
                print("Saved to reduced_dataset/eye_mouth_features.npy")
            break
        elif key == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_from_webcam_and_extract()
