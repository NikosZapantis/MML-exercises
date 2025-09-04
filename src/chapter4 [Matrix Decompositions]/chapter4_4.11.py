import sympy as sp

#! Sources: [https://docs.sympy.org/latest/modules/evalf.html / https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html] (evalf, eigenvals)

# Random A matrix (3x2)
A = sp.Matrix([[2, 1],
               [1, 3],
               [0, 1]])

print("\n~ 4.11 Theory (proof) ~")
print("\nMatrix A =")
sp.pprint(A)

# Calculating A^T * A & A * A^T
AtA = A.T * A
AAt = A * A.T

print("\nA^T * A =")
sp.pprint(AtA)

print("\nA * A^T =")
sp.pprint(AAt)

# Eigenvalues
eigenvals_AtA = [ev.evalf() for ev in AtA.eigenvals()]
eigenvals_AAt = [ev.evalf() for ev in AAt.eigenvals()]

# Displaying eigenvalues
print("\nEigenvalues of A^T * A:", eigenvals_AtA)
print("Eigenvalues of A * A^T:", eigenvals_AAt)
