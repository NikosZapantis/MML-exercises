import sympy as sp

#! Sources: [https://docs.sympy.org/latest/modules/matrices/expressions.html (for trace)]
#! From theory
#! For f(t) I used chain rule
#! For g(x) I know from trace theory (basically on chapter 4) --> tr(AB) = tr(BA)

#? f(t)
n = 3
t = sp.Matrix(sp.symbols('t0:%d' % n))
f = sp.sin(sp.log(t.dot(t)))
f_grad = sp.simplify(sp.Matrix([sp.diff(f, ti) for ti in t]))
print("\n~ 5.6 [f(t) & g(x)]")

# Display results
print("\n~ Results for f(t)\n")
print("f(t) =", f)
print("Gradient f(t) =", f_grad)

#? g(x)
a1, a2, a3 = 2, 2, 2
A = sp.MatrixSymbol('A', a1, a2)
X = sp.MatrixSymbol('X', a2, a3)
B = sp.MatrixSymbol('B', a3, a1)
g = sp.Trace(A*X*B)

# derivative with respect to x
dg_dx = sp.diff(g, X)

# Display results
print("\n~ Results for g(x)\n")
print("Derivative with respect to x =", dg_dx)
