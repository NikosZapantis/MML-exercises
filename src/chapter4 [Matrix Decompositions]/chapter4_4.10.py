import numpy as np

#! Sources: [https://numpy.org/doc/2.3/reference/generated/numpy.linalg.svd.html / https://numpy.org/doc/2.0/reference/generated/numpy.outer.html]

A = np.array([[3, 2, 2],
              [2, 3, -2]])

# Calculating SVD
U, S, Vt = np.linalg.svd(A)

# Rank-1 approximation
A_rank1 = S[0] * np.outer(U[:, 0], Vt[0, :])

# Displaying results
print("\n~ 4.10 Rank-1 Approximation ~")
print("\nRank-1 Approximation of A =\n", A_rank1)
