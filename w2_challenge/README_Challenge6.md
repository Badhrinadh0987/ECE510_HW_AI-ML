
# Challenge #6: Perceptron with Sigmoid Activation

## 🧠 Objective
Implement a simple perceptron (single-layer neural network) using the sigmoid activation function. The goal is to train the model using the Perceptron Learning Rule to perform logical operations: **NAND** and **XOR**.

---

## 📌 Tasks

### 1. Build a Perceptron
- Two input neurons
- One output neuron
- Sigmoid activation function

### 2. Apply the Perceptron Learning Rule
- Adjust weights based on prediction error
- Use the formula:

```
weight += learning_rate × error × input
bias += learning_rate × error
```

---

## 🔧 Tools and Platform
- Language: **Python**
- Libraries: `numpy` only (no external ML frameworks)
- Platform: Local Python environment or [Google Colab](https://colab.research.google.com)

---

## 📊 Logic Gates

### NAND
| Input | Output |
|-------|--------|
| 0 0   | 1      |
| 0 1   | 1      |
| 1 0   | 1      |
| 1 1   | 0      |

### XOR
| Input | Output |
|-------|--------|
| 0 0   | 0      |
| 0 1   | 1      |
| 1 0   | 1      |
| 1 1   | 0      |

> ❗Note: XOR cannot be learned using a single-layer perceptron due to its non-linear separability.

---

## 🧪 Output Example for NAND
```
Input: [0 0], Predicted: ~0.99
Input: [0 1], Predicted: ~0.98
Input: [1 0], Predicted: ~0.98
Input: [1 1], Predicted: ~0.02
```

---

## ✅ Learning Outcome
- You understand how to implement a perceptron from scratch.
- You apply the sigmoid function and perceptron learning rule.
- You experience why XOR needs multi-layer perceptrons.

---

## 📁 Files
- `perceptron_nand_xor.py`: Python code to train the perceptron
- `Challenge6_Perceptron_Documentation.docx`: Full explanation and code documentation

---

## 📚 References
- [Machine Learning Mastery - Sigmoid Function](https://machinelearningmastery.com/a-gentle-introduction-to-sigmoid-function/)
- [Neural Networks - YouTube Intro](https://www.youtube.com/watch?v=aircAruvnKk)

---
