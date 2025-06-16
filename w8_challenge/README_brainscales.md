# BrainScaleS-2 Neuromorphic Simulation

This repository demonstrates a basic simulation example run on the BrainScaleS-2 neuromorphic hardware platform.

## 📌 Overview

The experiment simulates a simple neural network on BrainScaleS-2 using PyNN and PyTorch. It includes:
- Loading a pre-trained network
- Evaluating it on a test dataset (e.g., MNIST or Yin-Yang)
- Observing neuron dynamics such as membrane potential and spiking behavior
- Measuring classification accuracy

## 🧪 Expected Output

Upon running the demo (e.g., `hwdemo.ipynb`), you should observe console output similar to:

```
Training 0 epochs -> duration: 0.234 seconds
test accuracy 0.943
```

Additionally, two visual outputs are generated:
- **Voltage Trace**: Time vs membrane voltage of a neuron
- **Spike Raster Plot**: Spiking activity across multiple neurons

## 🧠 Visualization Example

![Simulated Output](brainscales_sim_output.png)

## ▶️ How to Run on BrainScaleS-2

1. Clone the repository and install requirements:
   ```bash
   git clone <repo_url>
   cd fastAndDeep-main
   pip install -r requirements.txt
   ```

2. Launch Jupyter and open `src/hwdemo.ipynb`:
   ```bash
   jupyter notebook
   ```

3. Execute all cells to simulate the hardware inference.

## 📂 File Structure

- `src/hwdemo.ipynb`: Hardware simulation notebook
- `experiment_configs/`: Config files for training and inference
- `experiment_pretrained/`: Pretrained model weights

## 📞 Support

If you are running on EBRAINS or BrainScaleS systems, ensure the correct kernel is activated and the hardware interface is available.
