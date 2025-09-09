import sympy as sp

#! Used chain rule [log(x^4) = 4*log(x), x > 0] & [(sin(x^3))' = 3x^2 * cos(x^3)]
#! Sources: [https://docs.sympy.org/latest/modules/simplify/simplify.html]

x = sp.symbols('x')
f = sp.log(x**4) * sp.sin(x**3)
f_par = sp.simplify(sp.diff(f, x))

# Display results
print("\n~ 5.1 - Derivative of f(x) = log(x^4) * sin(x^3)")
print("\nf(x) =", f)
# sp.pprint(f) 
print("\nf'(x) =", f_par)
# sp.pprint(f_par)
