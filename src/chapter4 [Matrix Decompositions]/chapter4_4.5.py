import sympy as sp

#! Sources: [https://docs.sympy.org/latest/modules/matrices/matrices.html]

matrices = {
    "M1": sp.Matrix([[1, 0], [0, 1]]),
    "M2": sp.Matrix([[1, 0], [0, 0]]),
    "M3": sp.Matrix([[1, 1], [0, 1]]),
    "M4": sp.Matrix([[0, 1], [0, 0]])
}

print(f"\n~ 4.5 Diagonalizable / Invertible ~")
for name, M in matrices.items():
    print(f"\n{name} =")
    print(M)
    print("Determinant:", M.det())
    print("Is invertible?", M.det() != 0)
    print("Is diagonalizable?", M.is_diagonalizable())
