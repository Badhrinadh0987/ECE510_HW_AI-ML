#include <iostream>
#include <cuda.h>

// Helper macro to check for CUDA errors
#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)
{
    if (code != cudaSuccess) 
    {
        fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
        if (abort) exit(code);
    }
}

// CUDA kernel: 1 thread computes the Fibonacci sequence
__global__ void fibonacci_kernel(unsigned long long* fib, int N) {
    if (threadIdx.x == 0 && blockIdx.x == 0) {
        fib[0] = 0;
        if (N > 1) fib[1] = 1;

        for (int i = 2; i < N; i++) {
            fib[i] = fib[i-1] + fib[i-2];
        }
    }
}

// Sequential CPU version
void fibonacci_seq(unsigned long long* fib, int N) {
    fib[0] = 0;
    if (N > 1) fib[1] = 1;
    for (int i = 2; i < N; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
}

int main() {
    const int N = 220;
    unsigned long long *h_fib_seq = new unsigned long long[N];
    unsigned long long *h_fib_gpu = new unsigned long long[N];

    // CPU computation
    fibonacci_seq(h_fib_seq, N);

    // Allocate memory on GPU
    unsigned long long* d_fib;
    gpuErrchk(cudaMalloc((void**)&d_fib, N * sizeof(unsigned long long)));

    // 🔥 Important: Initialize device memory to 0
    gpuErrchk(cudaMemset(d_fib, 0, N * sizeof(unsigned long long)));

    // Launch kernel
    fibonacci_kernel<<<1, 1>>>(d_fib, N);

    // Check for errors
    gpuErrchk(cudaPeekAtLastError());
    gpuErrchk(cudaDeviceSynchronize());

    // Copy result back to host
    gpuErrchk(cudaMemcpy(h_fib_gpu, d_fib, N * sizeof(unsigned long long), cudaMemcpyDeviceToHost));

    // Compare CPU and GPU results
    bool correct = true;
    for (int i = 0; i < N; ++i) {
        if (h_fib_seq[i] != h_fib_gpu[i]) {
            correct = false;
            std::cout << "Mismatch at index " << i << ": CPU " << h_fib_seq[i] << " GPU " << h_fib_gpu[i] << std::endl;
            break;
        }
    }
    if (correct) {
        std::cout << "✅ CPU and GPU Fibonacci sequences match!" << std::endl;
    }

    // Print first 20 Fibonacci numbers
    for (int i = 0; i < 20; ++i) {
        std::cout << "F(" << i << ") = " << h_fib_gpu[i] << std::endl;
    }

    // Free memory
    cudaFree(d_fib);
    delete[] h_fib_seq;
    delete[] h_fib_gpu;

    return 0;
}
