
import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
import numpy as np

@cocotb.test()
async def run_test(dut):
    dut._log.info("Starting simulation")

    # Start 10ns-period clock on clk signal
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset
    dut.rst.value = 1
    dut.start.value = 0
    dut.in_index.value = 0
    dut.in_data.value = 0
    await Timer(20, units="ns")
    dut.rst.value = 0

    # Load feature data
    features = np.load("landmark_dataset/features.npy")[0]
    quantized = np.clip(np.round((features - 0.5) * 2 * 128), -128, 127).astype(np.int8)

    # Send input data
    for i, val in enumerate(quantized):
        dut.in_index.value = i
        dut.in_data.value = val & 0xFF
        await RisingEdge(dut.clk)

    # Start computation
    dut.start.value = 1
    await RisingEdge(dut.clk)
    dut.start.value = 0  # Deassert start

    # Wait for done signal
    for _ in range(300):
        await RisingEdge(dut.clk)
        if dut.done.value:
            break

    dut._log.info(f"Output Data = {dut.out_data.value}")
    assert dut.done.value == 1, "Computation did not finish in expected time"
