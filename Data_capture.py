from datetime import datetime
import cv2
import os
import time

# Create directories to store data
alert_dir = "dataset/alert"
drowsy_dir = "dataset/drowsy"

# Make sure directories exist
os.makedirs(alert_dir, exist_ok=True)
os.makedirs(drowsy_dir, exist_ok=True)

# Start video capture
cap = cv2.VideoCapture(0)

print("Press 'a' for Alert images, 'd' for Drowsy images, and 'q' to quit.")

while True:
    ret, frame = cap.read()
    
    # Display the webcam feed
    cv2.imshow("Webcam Feed", frame)

    # Wait for key press and take action
    key = cv2.waitKey(1) & 0xFF

    # Capture 'Alert' images
    if key == ord('a'):
        img_name = f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{int(time.time())}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Alert image saved as {img_name}")

    # Capture 'Drowsy' images
    elif key == ord('d'):
        img_name = f"{drowsy_dir}/drowsy_{int(time.time())}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Drowsy image saved as {img_name}")

    # Quit the capture loop
    elif key == ord('q'):
        break

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
