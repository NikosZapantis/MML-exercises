import sympy as sp

#! Sources: [https://en.wikipedia.org/wiki/Convex_conjugate / https://math.stackexchange.com/questions/5053586/fenchel-conjugate-of-a-quadratic-form-linear-form]
#! [https://en.wikipedia.org/wiki/Convex_set / https://docs.sympy.org/latest/modules/matrices/matrices.html (for LUsolve)]

n = 2
A11, A12, A22 = sp.symbols('A11 A12 A22', real=True)
A = sp.Matrix([[A11, A12], [A12, A22]])
b1, b2 = sp.symbols('b1 b2', real=True)
b = sp.Matrix([b1, b2])
s1, s2 = sp.symbols('s1 s2', real=True)
s = sp.Matrix([s1, s2])
c = sp.symbols('c', real=True)

x = sp.Matrix(sp.symbols('x1 x2', real=True))
f = sp.Rational(1, 2)*(x.T*A*x)[0] + (b.T*x)[0] + c

#? computing conjugate: maximize (s^Tx - f)
#? derivative with respect to x and solving -> x* = A^{-1}(s - b)

xstar = A.LUsolve(s - b) # or it could also be more analytic: A.inv()*(s - b)
fs = (s.T*xstar)[0] - (sp.Rational(1, 2)*(xstar.T*A*xstar)[0] + (b.T*xstar)[0] + c)

print("\n~ 7.10 Derive convex conjugate of f(x)")
print("f*(s) =", sp.simplify(fs))
