
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def load_dataset():
    X, y = [], []
    feature_dir = "dataset/features"
    label_dir = "dataset/labels"

    for fname in os.listdir(feature_dir):
        if fname.endswith(".npy"):
            features = np.load(os.path.join(feature_dir, fname))
            label_file = os.path.join(label_dir, fname.replace(".npy", ".txt"))
            if os.path.exists(label_file):
                with open(label_file, "r") as f:
                    label = int(f.read().strip())
                    X.append(features)
                    y.append(label)
    return np.array(X), np.array(y)

def train_and_save_model(X, y, model_type="mlp"):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if model_type == "svm":
        model = SVC(kernel="linear", probability=True)
    else:
        model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/drowsiness_classifier.pkl")
    print("✅ Model saved to model/drowsiness_classifier.pkl")

if __name__ == "__main__":
    X, y = load_dataset()
    if len(X) < 5:
        print("❗ Not enough data. Please collect more samples using collect_labeled_data.py")
    else:
        train_and_save_model(X, y, model_type="mlp")
