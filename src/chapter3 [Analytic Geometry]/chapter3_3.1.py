import sympy as sp

#! Sources [https://docs.sympy.org/latest/modules/simplify/simplify.html / https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html (for eigenvals)]

# Defining symbols
x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2', real=True)
x, y = sp.Matrix([x1, x2]), sp.Matrix([y1, y2])

# G array used to define inner product [symmetric]
G = sp.Matrix([[1, -1], 
               [-1, 2]])

# Inner product defined by G
inner = (x.T * G * y)[0]

#? Symmetry check [<x, y> - <y, x> = 0 OR <x, y> = <y, x>]
sym_check = sp.simplify(inner - (y.T * G * x)[0]) == 0

#? Calculating <x, x> for PD check
inner_xx = sp.simplify((x.T * G * x)[0])
inner_xx_factored = sp.factor(inner_xx)

#? Idiotimes of G (> 0)
eigenvalues = [ev.simplify() for ev in G.eigenvals().keys()]

# Displaying results
print("\n~ Inner product <x, y> =", inner)
print("\n~ Symmetry check (<x, y> = <y, x>):", sym_check)
print("\n\n~ <x, x> =", inner_xx_factored) # (x1 - x2)^2 + x2^2
print("\n~ Eigenvalues of G =", eigenvalues)
