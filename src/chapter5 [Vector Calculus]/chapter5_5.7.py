import sympy as sp

#! Sources: [https://www.geeksforgeeks.org/python/python-sympy-diag-method/ & https://math.libretexts.org/Bookshelves/Calculus/Supplemental_Modules_(Calculus)/Vector_Calculus/3%3A_Multiple_Integrals/3.8%3A_Jacobians]
#! From theory f(z) = sin(z) --> f'(z) is diag(cos(z))

print("\n~ 5.7 Derivatives")

#? a) f(z)
n = 3
x = sp.Matrix(sp.symbols('x0:%d' % n))
z = x.dot(x)
f_a = sp.log(1 + z)
f_a_grad = sp.Matrix([sp.diff(f_a, xi) for xi in x])

# Display results
print("\n~ Results for a)\n")
print("f(x) =", f_a)
print("Gradient with respect to x =", sp.simplify(f_a_grad))

#? b) f(z)
a1, a2 = 3, 2
A = sp.MatrixSymbol('A', a1, a2)
b = sp.MatrixSymbol('b', a1, 1)
x = sp.MatrixSymbol('x', a2, 1)
z = A*x + b
f_b = sp.sin(z)

# Computing jacobian
f_b_jac = sp.diag(*[sp.cos(zi) for zi in sp.Matrix(z)]) * A

# Display results
print("\n~ Results for b)\n")
print("Jacobian with respect to x =")
sp.pprint(f_b_jac)
