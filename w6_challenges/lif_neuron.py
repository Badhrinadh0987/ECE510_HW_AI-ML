import matplotlib.pyplot as plt

def binary_lif_neuron(inputs, leak=0.9, threshold=5):
    potential = 0
    spikes = []
    potentials = []

    for t, inp in enumerate(inputs):
        # Update potential with leak and input
        potential = leak * potential + inp

        if potential >= threshold:
            spikes.append(1)
            potential = 0  # Reset on spike
        else:
            spikes.append(0)

        potentials.append(potential)

    return spikes, potentials

# Example input sequences
inputs = [0]*5 + [1]*10 + [0]*10 + [1, 1, 1, 1, 1]
spikes, potentials = binary_lif_neuron(inputs)

# Plotting
plt.figure(figsize=(12, 4))
plt.subplot(2, 1, 1)
plt.plot(inputs, label='Input')
plt.plot(spikes, label='Spike', linestyle='--')
plt.legend()
plt.title("Binary LIF Neuron Output")

plt.subplot(2, 1, 2)
plt.plot(potentials, label='Potential', color='orange')
plt.axhline(y=5, color='r', linestyle=':', label='Threshold')
plt.legend()
plt.xlabel("Time step")
plt.tight_layout()
plt.show()
