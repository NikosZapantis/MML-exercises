import sympy as sp

#! Theory 
#! standard definition [1/N * S (xi - xˉ)^2]
#! raw-score expression [1/N * S xi^2 - xˉ^2]

#? [6.44) V[x] = E[x^2] - E[x]^2]
x0, x1, x2 = sp.symbols('x0 x1 x2')
x = [x0, x1, x2]
mean = sum(x)/3

# Calculating both left and right hands sides [so I can find the difference]
lhs = sum((xi-mean)**2 for xi in x)/3
rhs = sum(xi**2 for xi in x)/3 - mean**2

# Display results
print("\n~ 6.6 Prove the relationship in 6.44")
print("\nLHS =", sp.simplify(lhs))
print("\nRHS =", sp.simplify(rhs))
print("\nDiff =", sp.simplify(lhs - rhs))
