import numpy as np

#! Sources [https://numpy.org/doc/stable/reference/generated/numpy.allclose.html]
A = np.array([[2, 0], [1, 2]], dtype=float)
print("\n~ Is A symmetric?\n\tAnswer: ", np.allclose(A, A.T))
