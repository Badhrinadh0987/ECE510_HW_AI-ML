# CUDA Fibonacci Sequence (N = 220) — Google Colab Implementation & Debug Log

This project demonstrates how to compute the Fibonacci sequence using CUDA on a GPU-enabled Google Colab environment. It documents all debugging steps, errors encountered, and how each issue was resolved.

---

## 🚀 Objective

- Compute Fibonacci sequence up to N = 220 using CUDA
- Compare GPU result with a sequential CPU implementation
- Resolve execution issues due to Colab's driver/toolchain mismatch

---

## 📦 Files

- `fibonacci.cu` — Main CUDA implementation (host + kernel code)
- `README.md` — This file (full debugging + solution guide)

---

## 💡 Key Fixes and Takeaways

| Issue Encountered | Resolution |
|-------------------|------------|
| All GPU output = 0 | Added `cudaDeviceSynchronize()` |
| Race condition between threads | Used a **single thread** to compute full sequence |
| Memory not initialized | Zeroed memory with `cudaMemset()` |
| PTX toolchain mismatch | Compiled using `-arch=sm_75` for Tesla T4 compatibility |
| Silent CUDA API failures | Added `gpuErrchk()` macro for error tracing |

---

## ✅ Final Working CUDA Kernel

```cpp
__global__ void fibonacci_kernel(unsigned long long* fib, int N) {
    if (threadIdx.x == 0 && blockIdx.x == 0) {
        fib[0] = 0;
        if (N > 1) fib[1] = 1;
        for (int i = 2; i < N; i++) {
            fib[i] = fib[i-1] + fib[i-2];
        }
    }
}

#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true) {
    if (code != cudaSuccess) {
        fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
        if (abort) exit(code);
    }
}
```

---

## 🧪 Compile and Run (in Google Colab)

```bash
!nvcc -arch=sm_75 fibonacci.cu -o fibonacci
!./fibonacci
```

---

## 🎯 Final Outcome

- ✅ CUDA kernel executed correctly on **Tesla T4 GPU** in Google Colab
- ✅ GPU and CPU results matched for all 220 Fibonacci numbers
- ✅ All runtime errors, toolchain mismatches, and memory issues resolved

---

## 🧠 Learnings

- Always match `-arch` flag to your GPU’s compute capability (e.g., T4 → `sm_75`)
- CUDA kernels are asynchronous — use `cudaDeviceSynchronize()`
- Add runtime checks (`cudaGetErrorString`) to debug CUDA API calls
- Don’t parallelize Fibonacci naively — the computation is sequential by nature

---

> Developed and debugged entirely on Google Colab using Tesla T4 GPU and CUDA 12.3+.
