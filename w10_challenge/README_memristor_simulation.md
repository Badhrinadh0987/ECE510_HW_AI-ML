# Memristor Simulation (Challenge #28)

This project implements a memristor model using the **Biolek window function** in Python to generate the characteristic **pinched hysteresis I-V curve**, a key feature of memristive systems.

## 📌 Objective
Model and simulate a memristor using Python and plot the I-V curve to visualize the device’s behavior under sinusoidal excitation.

## 🧪 Methodology
- Memristor parameters are defined according to the Biolek model.
- A sinusoidal voltage input is applied.
- Current is calculated at each step based on dynamic resistance.
- The I-V curve is plotted to observe memristive behavior.

## 🔧 Parameters Used
- `R_on` = 100 Ohms
- `R_off` = 16,000 Ohms
- Thickness `D` = 10 nm
- Mobility `μ_v` = 1e-14 m²/s/V
- Time steps = 1000
- Input signal = 5 Hz sinusoid

## 📈 Output
The I-V curve displays the **pinched hysteresis loop**, verifying the memory-dependent resistance of the device.

![IV Curve](memristor_iv_curve.png)

## 📂 Files Included
- `memristor_sim.py`: Python script with simulation code
- `memristor_iv_curve.png`: Output plot
- `memristor_simulation_report.pdf`: Report of the simulation
- `memristor_simulation_report.docx`: Word version of the report

## 🚀 Run Instructions
```bash
python memristor_sim.py
```

## 🧠 Learning Outcome
This simulation demonstrates how memristors change resistance based on historical input, supporting their role as artificial synapses in neuromorphic computing.

---

**Author**: Badhrinadh Alladurgam  
**Course**: ECE 410/510, Spring 2025
