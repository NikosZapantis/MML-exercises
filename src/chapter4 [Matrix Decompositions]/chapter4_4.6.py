import sympy as sp

#! Sources: [https://docs.sympy.org/latest/modules/matrices/matrices.html]

A_a = sp.Matrix([[2, 3, 0],
               [1, 4, 3],
               [0, 0, 1]])

A_b = sp.Matrix([[1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]])

print("\n~ 4.6 Eigenspaces for transformation matrices ~")

def display_all(M, name):
    print(f"\nMatrix {name} =\n", M)
    eigenvects = M.eigenvects()
    for eigenval, alg_mult, eigenvecs in eigenvects:
        print(f"\nEigenvalue: {eigenval}, Algebraic Multiplicity: {alg_mult}")
        print("Geometric Multiplicity:", len(eigenvecs))
        for i, v in enumerate(eigenvecs, start=1):
            print(f"\tBasis vector {i}:", list(v))
        print("\nIs diagonalizable?", M.is_diagonalizable())

display_all(A_a, "A_a")
display_all(A_b, "A_b")
