import numpy as np
import matplotlib.pyplot as plt

# Constants and initial values
R_on = 100     # Low resistance (Ohm)
R_off = 16000  # High resistance (Ohm)
D = 10e-9      # Thickness of the memristor (m)
mu_v = 1e-14   # Ion mobility (m^2/s/V)
dt = 1e-5      # Time step
steps = 1000

# Time and voltage signal
time = np.linspace(0, 1, steps)
v = 1.5 * np.sin(2 * np.pi * 5 * time)  # Sinusoidal voltage

# Initialize
w = np.zeros(steps)
i = np.zeros(steps)
r = np.zeros(steps)
w[0] = 0.5 * D

for t in range(1, steps):
    # Memristance at current state
    r[t] = R_on * (w[t-1]/D) + R_off * (1 - w[t-1]/D)
    i[t] = v[t] / r[t]

    # Change in w using Biolek window function
    dw = mu_v * R_on * i[t] * dt
    if v[t] > 0:
        f = 1 - ((w[t-1]/D)**2)
    else:
        f = 1 - ((1 - w[t-1]/D)**2)
    w[t] = w[t-1] + dw * f

    # Keep w within bounds
    w[t] = max(0, min(D, w[t]))

# Plotting the I-V curve
plt.figure()
plt.plot(v, i)
plt.title("Memristor I-V Curve (Pinched Hysteresis Loop)")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.show()
