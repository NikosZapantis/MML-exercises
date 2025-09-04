import sympy as sp

#! Sources: [https://docs.sympy.org/latest/modules/matrices/matrices.html] (is_diagonalizable, eigenvects)

A = sp.Matrix([[0, -1,  1, 1],
               [-1, 1, -2, 3],
               [2, -1,  0, 0],
               [1, -1,  1, 0]])

print("\n~ 4.4 Eigenspaces ~")
print("\nMatrix A =\n", A)

# Calcuating eigenvalues and eigenvectors
eigenvects = A.eigenvects()
for eigenval, alg_mult, eigenvecs in eigenvects:
    print(f"\nEigenvalue: {eigenval}, Algebraic Multiplicity: {alg_mult}")
    print("Geometric Multiplicity:", len(eigenvecs))
    for i, v in enumerate(eigenvecs, start=1):
        print(f"\tBasis vector {i}:", list(v))

print("\nIs diagonalizable?", A.is_diagonalizable())   
