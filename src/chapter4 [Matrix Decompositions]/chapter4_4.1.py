import sympy as sp

#! Sources: [https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html]

A = sp.Matrix([[1, 3, 5], 
               [2, 4, 6],
               [0, 2, 4]])

# Calculating det with Laplace Expansion (1st row)
det_laplace = A.det(method='laplace')

# Calculating det with Sarrus' Rule [by default .det is sarrus]
det_sarrus = A.det()

# Displaying results
print("\n~ 4.1 Determinants ~")
print("\nMatrix A:")
sp.pprint(A)
print("\nDeterminant of A using Laplace Expansion:", det_laplace)
print("Determinant of A using Sarrus' Rule:", det_sarrus)
