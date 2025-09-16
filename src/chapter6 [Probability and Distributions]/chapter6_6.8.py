import sympy as sp

#! Sources: [https://en.wikipedia.org/wiki/Bernoulli_distribution / https://en.wikipedia.org/wiki/Exponential_family]
#! Theory [p(x | θ) = h(x) exp (⟨θ, ϕ(x)⟩ − A(θ))]

x, m = sp.symbols('x m')
h = sp.log(m/(1 - m))
A = sp.log(1 + sp.exp(h))

exp1 = sp.simplify(sp.exp(h*x - A))
exp2 = sp.simplify(m**x * (1 - m)**(1 - x))

# Display results
print("\n~ 6.8 Express the Bernoulli distribution 6.107")
print("\nExponential-family form =", exp1)
print("\nOG Bernoulli =", exp2)
print("\nRatio =", sp.simplify(exp1/exp2))
