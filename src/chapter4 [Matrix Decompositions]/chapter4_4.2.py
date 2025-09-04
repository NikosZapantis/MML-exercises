import sympy as sp

#! Sources: [https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html]

B = sp.Matrix([[2, 0, 1, 2, 0],
               [2, -1, 0, 1, 1],
               [0, 1, 2, 1, 2],
               [-2, 0, 2, -1, 2],
               [2, 0, 0, 1, 1]])

# Calculating det
det_B = B.det()

# Displaying results
print("\n~ 4.2 Determinants ~")
print("\nMatrix B:")
sp.pprint(B)
print("\nDeterminant of B:", det_B)
