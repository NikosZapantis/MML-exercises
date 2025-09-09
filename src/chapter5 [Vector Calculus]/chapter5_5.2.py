import sympy as sp

#! Used chain rule [(1/(1+e^(-x)))' = e^(-x) / (1 + e^(-x))^2]
#! Sources: [https://docs.sympy.org/latest/modules/simplify/simplify.html]

x = sp.symbols('x')
f = 1/(1 + sp.exp(-x))
f_par = sp.simplify(sp.diff(f, x))

# Display results
print("\n~ 5.2 - Derivative of f(x) = 1 / (1 + e^(-x))")
print("\nf(x) =", f)
# sp.pprint(f)
print("\nf'(x) =", f_par)
# sp.pprint(f_par)
