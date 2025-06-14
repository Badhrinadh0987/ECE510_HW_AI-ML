import time
import numpy as np
import matplotlib.pyplot as plt

def systolic_bubble_sort(arr):
    n = len(arr)
    pe_array = list(arr)
    for phase in range(n):
        for i in range(n - 1):
            if pe_array[i] > pe_array[i + 1]:
                pe_array[i], pe_array[i + 1] = pe_array[i + 1], pe_array[i]
    return pe_array

def benchmark_systolic_sort(sizes):
    times = []
    for size in sizes:
        arr = np.random.randint(0, 1000000, size=size)
        start = time.time()
        systolic_bubble_sort(arr)
        end = time.time()
        times.append(end - start)
    return times

sizes = [10, 100, 1000, 2000]
timings = benchmark_systolic_sort(sizes)

plt.plot(sizes, timings, marker='o')
plt.title("Systolic Bubble Sort Execution Time")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.grid(True)
plt.show()
