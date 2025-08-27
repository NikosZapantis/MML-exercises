import numpy as np
from sympy import Matrix, symbols, Rational

#? [Check https://stackoverflow.com/questions/15638650/is-there-a-standard-solution-for-gauss-elimination-in-python & https://www.geeksforgeeks.org/dsa/gaussian-elimination/]
#! Sources used [https://docs.sympy.org/latest/explanation/best-practices.html#] sympy documentation

print("~ 2.6 Solving Linear Systems Ax = b using Gaussian Elimination [NumPy & SymPy] ~")

# Defining systems A and b
A = np.array([[0, 1, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 1]], dtype=float)
b = np.array([2, -1, 1], dtype=float)

print("Matrix A:", A)
print("Vector b:", b)

# Converting to SymPy Matrix for rref
M = Matrix(np.column_stack((A, b))).applyfunc(Rational) # Matrix [A | b]

print("\nAugmented Matrix [A | b]:", M)

# Computing RREF
rref_matrix, pivot_columns = M.rref()

print("\nRREF of the augmented matrix:", rref_matrix)
print("\nPivot columns:", pivot_columns)

# Solutions by RREF
num_vars = A.shape[1]
sym_vars = symbols(f"x0:{num_vars}")
sol_expr = {var: None for var in sym_vars}

# Solutions from rref
for i, pivot_col in enumerate(pivot_columns):
    # equation: x[pivot_col] + sum(coeff * free_var) = constant
    expr = rref_matrix[i, -1]

    # coefficients for free variables
    for j in range(num_vars):
        if j != pivot_col:
            coeff = rref_matrix[i, j]
            if coeff != 0:
                expr -= coeff * sym_vars[j]
    sol_expr[sym_vars[pivot_col]] = expr

# Assigning free vars
for j in range(num_vars):
    if sym_vars[j] not in sol_expr or sol_expr[sym_vars[j]] is None:
        sol_expr[sym_vars[j]] = sym_vars[j]

print("\nSolution expressions:")
for var in sym_vars:
    print(f"{var} = {sol_expr[var]}")

sol_vector = Matrix([sol_expr[var] for var in sym_vars])
print("\nSolution vector:", sol_vector)

