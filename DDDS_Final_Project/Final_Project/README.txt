
🧠 DRIVER DROWSINESS DETECTION SYSTEM — HYBRID ML + RTL ACCELERATION
====================================================================

This project detects driver drowsiness using facial landmark features (eyes + mouth) 
with two pipelines:
 - ML Classifier-based live detection
 - Hardware-accelerated MAC computation for feature comparison

📁 PROJECT STRUCTURE
---------------------
- `collect_labeled_data.py`   : Capture labeled eye+mouth features from webcam
- `train_classifier.py`       : Train MLP classifier on labeled feature data
- `classify_live.py`          : Run real-time detection using trained model
- `run_hw_acceleration.py`    : Preprocess features, quantize, generate .mem files
- `rtl/`                      : Verilog RTL for MAC+ReLU pipeline
- `sim_build/`                : Testbench + Makefile-based simulation
- `model/`                    : Contains trained ML model
- `dataset/`                  : Collected .npy feature files + labels
- `mem_files/`                : Memory files used in RTL (features.mem, golden.mem)
- `reduced_dataset/`          : Last extracted features from webcam

📌 REQUIREMENTS
---------------
- Python 3.x
- `opencv-python`, `dlib`, `numpy`, `scikit-learn`, `joblib`
- ModelSim (for RTL simulation)

⚙️ USAGE FLOW
-------------
1. Collect Training Data:
   python3 collect_labeled_data.py
   - Press 'A' for alert, 'D' for drowsy, 'ESC' to quit

2. Train Classifier:
   python3 train_classifier.py

3. Run Live Detection:
   python3 classify_live.py

4. Generate RTL Inputs and Compare:
   python3 run_hw_acceleration.py
   (Then run `make` in the `sim_build/` directory via ModelSim)

💡 NOTE:
---------
All memory files are auto-generated in `mem_files/`
Trained classifier is saved to `model/drowsiness_classifier.pkl`

Author: ChatGPT Integration on request
