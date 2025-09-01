import numpy as np

#! Sources [https://numpy.org/doc/2.3/reference/generated/numpy.linalg.norm.html]

x = np.array([1, 2, 3.], float)
y = np.array([-1, -1, 0.], float)

A = np.array([[2, 1, 0], 
              [1, 3, -1], 
              [0, -1, 2.]], float)

# Finding both a) Euclidean [Dot product] and b) inner product A
diff = x - y

# a) Euclidean distance sqrt((x - y)^T (x - y))
d_euclidean = np.linalg.norm(diff)

# b) Distance defined by A sqrt((x - y)^T A (x - y))
d_A = np.sqrt(diff @ A @ diff)

# Displaying results
print(f"\na) Euclidean distance: {d_euclidean:.4f}")
print(f"b) Distance (inner product) defined by A: {d_A:.4f}\n")
