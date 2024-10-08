import random
import time
import numpy as np

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

    # Esecuzione del benchmark
    start_time = time.time()
    matrix_multiplication(A, B)
    end_time = time.time()

    # Stampa del tempo di esecuzione
    print(f"Dimensione matrice: {n}x{n} - Tempo di esecuzione: {end_time - start_time:.6f} secondi")

# Esegui il benchmark per diverse dimensioni
for size in [10, 100, 512, 1024, 2048]:
    benchmark_matrix_multiplication(size)
