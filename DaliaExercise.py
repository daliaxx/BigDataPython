import random
import time
import psutil
import os
import matplotlib.pyplot as plt

def generate_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def matrix_multiplication(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def benchmark_matrix_multiplication(n):
    # Generazione delle matrici
    A = generate_matrix(n)
    B = generate_matrix(n)

    # Misura della memoria prima dell'esecuzione
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024 / 1024  # Memoria in MB

    # Esecuzione del benchmark
    start_time = time.time()
    matrix_multiplication(A, B)
    end_time = time.time()

    # Misura della memoria dopo l'esecuzione
    mem_after = process.memory_info().rss / 1024 / 1024  # Memoria in MB

    # Calcolo del tempo di esecuzione e della memoria usata
    execution_time = end_time - start_time
    memory_used = mem_after - mem_before

    # Ritorno dei risultati
    return execution_time, memory_used

# Dimensioni delle matrici da testare
matrix_sizes = [10, 100, 512, 1024]

# Liste per salvare i tempi di esecuzione e la memoria usata
execution_times = []
memory_usages = []

# Esegui il benchmark per ogni dimensione
for size in matrix_sizes:
    exec_time, mem_used = benchmark_matrix_multiplication(size)
    execution_times.append(exec_time)
    memory_usages.append(mem_used)
    print(f"Matrix Size: {size}x{size} - Execution Time: {exec_time:.6f} seconds - Memory Used: {mem_used:.2f} MB")

# Creazione dei grafici
plt.figure(figsize=(10, 5))

# Grafico del tempo di esecuzione
plt.subplot(1, 2, 1)
plt.plot(matrix_sizes, execution_times, marker='o')
plt.title('Execution Time vs Matrix Size')
plt.xlabel('Matrix Size (NxN)')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)

# Grafico dell'uso della memoria
plt.subplot(1, 2, 2)
plt.plot(matrix_sizes, memory_usages, marker='o', color='orange')
plt.title('Memory Usage vs Matrix Size')
plt.xlabel('Matrix Size (NxN)')
plt.ylabel('Memory Usage (MB)')
plt.grid(True)

# Mostra i grafici
plt.tight_layout()
plt.show()
