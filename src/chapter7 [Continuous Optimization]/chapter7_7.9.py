import sympy as sp

#! Sources: [https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html]
#! [https://en.wikipedia.org/wiki/Entropy_(information_theory)]

n = 3
s = sp.symbols('s0:%d' % n, real=True)

# symb sum of e^(s_i - 1)
fs = sum(sp.exp(si - 1) for si in s)
sp.simplify(fs)

# Display outputs
print("\n~ 7.9 Convex conjugate f*(s)")
print("f*(s) =", sp.srepr(sp.simplify(fs))) # internally look
print("Close form:", sp.simplify(fs))
