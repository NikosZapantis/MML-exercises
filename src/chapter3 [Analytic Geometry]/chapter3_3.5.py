import numpy as np

#! Sources [https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html / https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html]

u1 = np.array([0, -1, 2, 0, 2], dtype=float)
u2 = np.array([1, -3, 1, -1, 2], dtype=float)
u3 = np.array([-3, 4, 1, 2, 1], dtype=float)
u4 = np.array([-1, -3, 5, 0, 7], dtype=float)

#? Defining matrix U with column vectors u1, u2, u3, u4
U = np.column_stack([u1, u2, u3, u4])
x = np.array([-1, -9, -1, 4, 1], dtype=float)

#? Calculating projection (pseudo-inverse)
proj = U @ np.linalg.pinv(U) @ x

# Distance
residual = x - proj
dist = np.linalg.norm(residual)

# Displaying results
print("\n~ 3.5 Projection (orthogonal) & Distance")
print("\nProjection π_U(x) =", proj)
print(f"\nDistance d(x, U) = {dist:.12f}")
