
import numpy as np
import os

# Load weights
weights_path = os.path.join("mem_files", "weights.npy")
weights = np.load(weights_path)

# Write to mem file in hex
output_path = os.path.join("mem_files", "weights.mem")
with open(output_path, "w") as f:
    for w in weights:
        f.write(f"{int(w):02x}\n")

print(f"Generated weights.mem with {len(weights)} entries.")
