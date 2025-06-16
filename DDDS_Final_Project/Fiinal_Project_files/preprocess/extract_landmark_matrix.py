import cv2 
import dlib 
import numpy as np 
import os
from imutils import face_utils
import time

# Paths
output_dir = "landmark_dataset"
os.makedirs(output_dir, exist_ok=True)

# Initialize face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)
features = []
labels = []  # 0 = alert, 1 = drowsy

print("Press 'a' for Alert, 'd' for Drowsy, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        vector = face_utils.shape_to_np(shape).flatten()  # shape: (136,)

        cv2.imshow("Webcam Feed", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('a'):
            features.append(vector)
            labels.append(0)
            print("Saved alert sample")

        elif key == ord('d'):
            features.append(vector)
            labels.append(1)
            print("Saved drowsy sample")

        elif key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

# Save feature and label arrays
np.save(os.path.join(output_dir, "features.npy"), np.array(features))
np.save(os.path.join(output_dir, "labels.npy"), np.array(labels))
print("Features and labels saved.")