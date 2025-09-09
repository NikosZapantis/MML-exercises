import sympy as sp

#! Used chain rule [If f(x) = e^g(x) => f'(x) = g'(x)e^g(x)] & [gx(x) = - (x - m)^2 / (2*s^2) => g'x(x) = - (x - m) / (s^2)]
#! Sources: [https://docs.sympy.org/latest/modules/simplify/simplify.html]

x, m, s = sp.symbols('x m s')
f = sp.exp(- (x - m)**2 / (2*s**2))
f_par = sp.simplify(sp.diff(f, x))

# Display results
print("\n~ 5.3 - Derivative of f(x) = exp(- (x - m)^2 / (2*s^2))")
print("\nf(x) =", f)
# sp.pprint(f)
print("\nf'(x) =", f_par)
# sp.pprint(f_par)
