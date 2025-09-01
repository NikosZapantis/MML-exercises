import numpy as np

#? 2.3 Check if (G, ·) abelian group

# Constructing 3x3 matrices of the form G as given in the book:
def matrix(x, y, z):
    return np.array([[1, x, z],
                    [0, 1, y],
                    [0, 0, 1]], dtype=int)

# Example matrices at G form
mat1 = matrix(1, 0, 0)
mat2 = matrix(0, 1, 0)

print("~ 2.3 Check if (G, ·) abelian group [Tables] ~")
print("\nMatrix #1:\n", mat1)
print("\nMatrix #2:\n", mat2)
print("\nmat1*mat2 =\n", mat1 @ mat2)
print("\nmat2*mat1 =\n", mat2 @ mat1)

# Checking commutativity [if !commutative, then group is not abelian]
print("\nCheck mat1*mat2 == mat2*mat1 \n\t Result: ", np.array_equal(mat1 @ mat2, mat2 @ mat1)) # False == not abelian
