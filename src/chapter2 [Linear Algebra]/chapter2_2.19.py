import numpy as np
from sympy import Matrix, pprint

print("~ 2.19 Endomorphism Φ: R^3 → R^3 ~")

# Transformation matrix respect to standard basis
A = np.array([[1, 1, 0],
              [1, -1, 0],
              [1, 1, 1]], dtype=int)

print("\nTransformation Matrix A (standard basis):")
print(A)

# Converting to SymPy Matrix for kernel and image
M = Matrix(A)

# Kernel
ker = M.nullspace()
print("\nKernel of Φ (basic vectors):")
if ker:
    ker_matrix = Matrix.hstack(*ker)
    pprint(ker_matrix)
else:
    print("{0}")

print("dim(ker(Φ)):", len(ker))

# Image
img = M.columnspace()
print("\nImage of Φ (basic vectors):")
img_matrix = Matrix.hstack(*img)
pprint(img_matrix)

print("dim(Im(Φ)):", len(img))

# Basis change
print("\n\n~ Basis change with respect to basis B")
B = Matrix([[1, 1, 1],
            [1, 2, 0],
            [1, 1, 0]])

print("\n Basis matrix B:")
pprint(B)

#! Change of basis: Af = B^-1 * A * B [Source that may have a better sol: https://www.kaggle.com/code/dhgupta/change-of-basis]
Af = B.inv() * M * B

print("\nTransformation Matrix A_B (basis B):")
pprint(Af)
