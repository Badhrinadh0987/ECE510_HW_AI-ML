import numpy as np
import matplotlib.pyplot as plt

# Define 4x4 resistance matrix (example weights)
weights = np.array([
    [1, 2, 1, 2],
    [2, 1, 2, 1],
    [1, 1, 1, 1],
    [2, 1, 2, 1]
])

# Convert to conductance matrix
conductance_matrix = 1 / weights

# Input vector
input_vector = np.array([1, 0, 1, 0])
output_currents = conductance_matrix.T @ input_vector

# Print for verification
print("Conductance Matrix:\n", conductance_matrix)
print("Input Vector:\n", input_vector)
print("Output Currents:\n", output_currents)

# ---------------------------
# 🖼️ Visualization
# ---------------------------

plt.figure(figsize=(12, 5))

# Heatmap of Conductance Matrix
plt.subplot(1, 2, 1)
plt.imshow(conductance_matrix, cmap='Blues', aspect='auto')
plt.colorbar(label='Conductance (1/R)')
plt.title("4x4 Conductance Matrix")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.xticks(np.arange(4))
plt.yticks(np.arange(4))

# Output Current Bar Chart
plt.subplot(1, 2, 2)
plt.bar(np.arange(4), output_currents, color='orange')
plt.title("Output Currents (Matrix-Vector Product)")
plt.xlabel("Output Node Index")
plt.ylabel("Current (Arbitrary Units)")
plt.xticks(np.arange(4))

plt.tight_layout()
plt.show()
