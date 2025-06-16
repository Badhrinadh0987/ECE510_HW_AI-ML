
import numpy as np
import os

os.makedirs("mem_files", exist_ok=True)

features = np.load("sim/landmark_dataset/features.npy")[0]
weights = np.random.randint(-128, 128, size=136).astype(np.int8)

# Quantize features
quantized = np.clip(np.round((features - 0.5) * 2 * 128), -128, 127).astype(np.int8)
dot = np.dot(quantized, weights)
golden_out = max(0, int(dot)) & 0xFF

# Save .mem files
with open("mem_files/features.mem", "w") as f:
    for val in quantized:
        f.write(f"{val & 0xFF:02x}\n")

with open("mem_files/golden.mem", "w") as f:
    f.write(f"{golden_out:02x}\n")

np.save("mem_files/weights.npy", weights)
print("Generated features.mem, golden.mem, and weights.npy in 'mem_files/' directory.")
