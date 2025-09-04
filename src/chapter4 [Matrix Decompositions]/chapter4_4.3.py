import sympy as sp

#! Sources: [https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html] (eigenvects returns eigenvalues/multiplicity/[eigenvectors])

A = sp.Matrix([[1, 0], 
               [1, 1]])

B = sp.Matrix([[-2, 2], 
               [2, 1]])

# Calculating eigenvectors for both a) and b)
eigs_A = A.eigenvects()
eigs_B = B.eigenvects()

# Displaying results
print("\n~ 4.3 Eigenspaces ~")
print("\nMatrix A:")
sp.pprint(A)
print("\nEigenvalues and Eigenvectors of A:")
for val, mult, vects in eigs_A:
    print(f"λ: {val}, Multiplicity: {mult}, Eigenspace basis: {vects}")

print("\n\nMatrix B:")
sp.pprint(B)
print("\nEigenvalues and Eigenvectors of B:")
for val, mult, vects in eigs_B:
    print(f"λ: {val}, Multiplicity: {mult}, Eigenspace basis: {vects}")
