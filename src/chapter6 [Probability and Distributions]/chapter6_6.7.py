import sympy as sp

#! Theory [We see that (6.45) is twice the raw-score expression]

x0, x1, x2 = sp.symbols('x0 x1 x2')
x = [x0, x1, x2]
mean = sum(x)/3

lhs = sum((x[i] - x[j])**2 for i in range(3) for j in range(i+1, 3))
rhs = 3 * sum((xi-mean)**2 for xi in x)

# Display results
print("\n~ 6.7 Prove the relationship in 6.45")
print("\nLHS =", sp.simplify(lhs))
print("\nRHS =", sp.simplify(rhs))
print("\nDiff =", sp.simplify(lhs - rhs))
