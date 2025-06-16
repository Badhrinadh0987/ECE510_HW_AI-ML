import numpy as np
import os

# Load feature matrix
features_path = "landmark_dataset/features.npy"
features = np.load(features_path)

# Optional: Normalize to [-1, 1]
features = 2 * (features - 0.5)  # if not already normalized

# Quantize: float to Q1.7 format → int8
scale = 128
quantized = np.clip(np.round(features * scale), -128, 127).astype(np.int8)

# Write each byte to .mem file (hex format)
output_path = "landmark_features.mem"
with open(output_path, "w") as f:
    for row in quantized:
        for val in row:
            f.write(f"{val & 0xFF:02X}\n")  # write hex byte

print(f".mem file generated at: {os.path.abspath(output_path)}")
