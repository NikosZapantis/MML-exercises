import numpy as np
from sympy import Matrix, pprint

print("~ 2.17 Linear Mapping Φ: R^3 → R^4 ~")

# Transformation matrix
A = np.array([[3, 2, 1],
              [1, 1, 1],
              [1, -3, 0],
              [2, 3, 1]], dtype=int)

print("\nTransformation Matrix A (4x3):")
print(A)

# Rank [https://numpy.org/doc/2.1/reference/generated/numpy.linalg.matrix_rank.html]
r = np.linalg.matrix_rank(A)
print("Rank of AΦ:", r)

# Converting to SymPy Matrix for kernel and image
M = Matrix(A)

# Kernel
ker = M.nullspace()
print("\nKernel of Φ (basic vectors):")
if ker:
    for v in ker:
        pprint(v)
else:
    print("{0}")

print("dim(ker(Φ)):", len(ker))

#! Image [Source: https://docs.sympy.org/latest/modules/matrices/matrices.html & ]
img = M.columnspace()
print("\nImage of Φ (basic vectors):")
img_matrix = Matrix.hstack(*img)
pprint(img_matrix)

print("dim(Im(Φ)):", len(img))

# Rank-Nullity check
n = A.shape[1]
print(f"\n/-- Check: dim(ker) + rank = {len(ker)} + {r} = {len(ker) + r} == {n}")
