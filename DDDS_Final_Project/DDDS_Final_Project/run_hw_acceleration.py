
import os
import numpy as np
from preprocess.extract_eye_mouth_features import capture_from_webcam_and_extract

print("Step 1: Capturing facial landmarks (eyes + mouth)...")
capture_from_webcam_and_extract()

print("Step 2: Quantizing and generating memory input/output files...")

features = np.load("reduced_dataset/eye_mouth_features.npy")
weights = np.random.randint(-128, 128, size=features.shape[0]).astype(np.int8)

quantized = np.clip(np.round((features - 0.5) * 2 * 128), -128, 127).astype(np.int8)
dot = np.dot(quantized, weights)
golden_out = max(0, int(dot)) & 0xFF

os.makedirs("mem_files", exist_ok=True)
with open("mem_files/features.mem", "w") as f:
    for val in quantized:
        f.write(f"{val & 0xFF:02x}\n")

with open("mem_files/golden.mem", "w") as f:
    f.write(f"{golden_out:02x}\n")

np.save("mem_files/weights.npy", weights)

print("✅ Generated: mem_files/features.mem, golden.mem")
print("\n📌 Now run the following command manually to simulate the RTL:")
print("   make")
print("📌 Then check the simulation output for PASS/FAIL.")
