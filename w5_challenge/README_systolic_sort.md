# Systolic Array Bubble Sort (Challenge #17)

This project implements **Bubble Sort** on a simulated **systolic array** and benchmarks its performance using various input sizes.

## 💡 Description

A systolic array is a grid of processing elements that rhythmically compute and pass data through the array. In this simulation:

- Each array element (PE) acts as a comparator and swaps with its neighbor.
- Bubble sort behavior is mimicked over `n` passes.
- Performance is benchmarked on increasing array sizes.

## 📂 Files Included

- `systolic_sort.py` – Main Python script with sorting logic and performance benchmark.
- `benchmark_results.csv` – Optional output for time results (if enabled).
- `Challenge17_SystolicSort_Documentation.docx` – Full documentation of the problem and implementation.
- `requirements.txt` – Python dependencies.

## 🚀 How to Run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the program:
    ```bash
    python systolic_sort.py
    ```

3. A graph will display showing time vs input size.

## 📈 Performance Benchmarking

Input sizes tested: 10, 100, 500, 1000, 2000  
Execution times are measured and plotted using `matplotlib`.

## 📊 Example Output

Graph:  
- X-axis: Input size  
- Y-axis: Execution time in seconds  
- Each dot represents the average time over multiple trials

## 🛠 Dependencies

- Python 3.x
- numpy
- matplotlib

## 📄 License

This project is for academic use as part of ECE 410/510 at Portland State University.
