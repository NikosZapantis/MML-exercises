import sympy as sp

#! Sources: [https://docs.sympy.org/latest/modules/simplify/simplify.html & https://docs.sympy.org/latest/modules/series/series.html]

x = sp.symbols('x')
f = sp.sin(x) + sp.cos(x)

# Display results
print("\n~ 5.4 - Taylor polynomials at x0 = 0 of f(x) = sin(x) + cos(x)")

# Example for n = 0 the f'(x) = cos(x) - sin(x) => f'(0) = 1
for n in range(6):
    Tn = sp.series(f, x, 0, n+1).removeO()
    print(f"\nT_{n}(x) = ", end="")
    f_next_par = sp.simplify(Tn)
    print(f_next_par)
