import sympy as sp

#! Sources: [https://hbunyamin.github.io/data-science-1/Natural_Parameter/]

n, k, a, b = sp.symbols('n k a b', positive=True)
m = sp.symbols('m')

print("\n~ 6.9 Binomial distribution")

#? a) Binomial distribution
bin_exp = sp.binomial(n, k) * m**k * (1 - m)**(n - k)
h = sp.log(m/(1 - m))
A_h = n * sp.log(1 + sp.exp(h))
expo_bin = sp.binomial(n, k) * sp.exp(h * k - A_h)

print("\na) Binomial as exponential family")
print("Ratio =", sp.simplify(expo_bin / bin_exp))

#? b) Beta distribution
beta_exp = m**(a - 1) * (1 - m)**(b - 1) / sp.beta(a, b)
expo_beta = sp.exp((a - 1) * sp.log(m) + (b - 1) * sp.log(1 -m) - sp.log(sp.beta(a, b)))

print("\nb) Beta distribution as exponential family")
print("Ratio =", sp.simplify(expo_beta / beta_exp))

#? c) Product of Beta and Binomial
prod = beta_exp * bin_exp
tar_beta = m**(a + k - 1) * (1 - m)**(b + n - k - 1) / sp.beta(a + k, b + n - k)
c = sp.simplify(prod / tar_beta)

print("\nc) Product of beta and binom")
print("Constant =", c) # not based on m
print("dC/dm =", sp.simplify(sp.diff(c, m))) # based on m
