import numpy as np

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training data for NAND
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
targets = np.array([[1],[1],[1],[0]]) # NAND truth table

# Initialize weights and bias
weights = np.random.rand(2)
bias = np.random.rand(1)

# Learning rate
lr = 0.1

# Training loop
for epoch in range(10000):
    for i in range(len(inputs)):
        # Forward pass
        x = inputs[i]
        y = targets[i]
        z = np.dot(x, weights) + bias
        output = sigmoid(z)

        # Error
        error = y - output

        # Backpropagation
        weights += lr * error * x
        bias += lr * error

# Testing
for i in range(len(inputs)):
    x = inputs[i]
    z = np.dot(x, weights) + bias
    output = sigmoid(z)
    print(f"Input: {x}, Predicted: {output}")
