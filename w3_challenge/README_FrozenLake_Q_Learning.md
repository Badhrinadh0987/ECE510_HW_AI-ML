
# 🧊 Q-Learning: FrozenLake-v1 Solver (with Hardware Bottleneck Analysis)

This project implements a Q-Learning agent to solve the `FrozenLake-v1` environment from OpenAI Gym. It includes:
- A complete Python implementation
- Debugging fixes for modern `gym` and `numpy`
- Episode-wise logging to a transcript/output file
- Identification of computational bottlenecks
- A SystemVerilog hardware accelerator for the `argmax` operation

---

## 📌 Environment Setup

Install dependencies:

```bash
pip install gym numpy
```

For compatibility:
- `gym >= 0.26`
- `numpy >= 1.24` (recommended with gym upgrades)

---

## 🚀 How to Run

Run the Python script:

```bash
python frozen_lake_q_learning.py
```

To save terminal output to a transcript file:

```bash
python frozen_lake_q_learning.py > transcript.txt
```

To see the output live and save it:

```bash
python frozen_lake_q_learning.py | tee transcript.txt
```

---

## 🧠 Algorithm Overview

The Q-Learning update rule:

```
Q[state, action] = Q[state, action] + α * (reward + γ * max(Q[next_state, :]) - Q[state, action])
```

---

## 📂 Output

- **`frozenlake_output.txt`**: Training log with average rewards and final Q-table
- **`transcript.txt`** (optional): Full stdout terminal log

Example snippet:
```
Episode 100: Avg Reward (last 100) = 0.04
Episode 200: Avg Reward (last 100) = 0.12
...
Training completed.
Overall average reward: 0.42
```

---

## 🔍 Identified Bottlenecks

Two major bottlenecks in the training loop:
- `np.argmax(Q[state, :])`: Used for action selection
- `np.max(Q[new_state, :])`: Used for Q-table update

These require scanning all action values and become significant in large environments.

---

## ⚙️ Hardware Acceleration (SystemVerilog)

A custom hardware module was proposed and written to accelerate the `argmax` operation using a comparator tree.

### Example:

```verilog
module max_finder_4 (
    input  logic [15:0] q0, q1, q2, q3,
    output logic [15:0] max_val,
    output logic [1:0]  max_idx
);
// Compares inputs and returns max value and index
endmodule
```

Useful for FPGA/ASIC acceleration of action selection.

---

## 📈 Debugging Summary

| Issue | Fix |
|------|-----|
| `ModuleNotFoundError: gym` | `pip install gym` |
| `IndexError` on Q[state, :] | Use `state, _ = env.reset()` |
| `AttributeError: numpy has no attribute 'bool8'` | Upgrade gym OR downgrade numpy |

---

## 📜 Credits

Based on Q-Learning logic from:
https://github.com/ronanmmurphy/Q-Learning-Algorithm

SystemVerilog hardware designed by: `Badhrinadh Alladurgam`

LLM-assisted documentation and analysis provided by OpenAI ChatGPT.

---

## 📄 License

This project is provided under the MIT License.
