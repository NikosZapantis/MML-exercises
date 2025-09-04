import numpy as np

#! Sources: [https://numpy.org/doc/2.3/reference/generated/numpy.linalg.svd.html]

A = np.array([[3, 2, 2],
              [2, 3, -2]])

# Calculating SVD
U, S, Vt = np.linalg.svd(A)

# Displaying results
print("\n~ 4.8 Singular Value Decomposition (SVD) ~")
print("\nU =\n", U)
print("\nS =\n", S)
print("\nVt =\n", Vt)
