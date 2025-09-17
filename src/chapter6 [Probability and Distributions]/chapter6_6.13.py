import numpy as np
import sympy as sp
from scipy.special import erf

#! Sources: [https://matthewfeickert.github.io/Statistics-Notes/notebooks/Introductory/probability-integral-transform.html]
#! [https://docs.sympy.org/latest/modules/utilities/lambdify.html]
#! Gauss error function [.erf]: [https://docs.sympy.org/latest/modules/functions/special.html]

#? Symbolic cumulative distr function 
x = sp.symbols('x', real=True)
F_start = sp.Rational(1, 2) * (1 + sp.erf(x / sp.sqrt(2)))

# Due to conflict with erf from sympy I used [https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.erf.html]
F = sp.lambdify(x, F_start, modules={"erf": erf, "numpy": np})

# transform
rng = np.random.default_rng(12345)
N = 200000
X = rng.normal(loc=0.0, scale=1.0, size=N)
Y = F(X) # Y = F_x(X)

mean_Y = Y.mean() # mean of Y
var_Y = Y.var(ddof=0) # variance

# Display results
print("\n~ 6.13 Theorem 6.15 Porbability Integral Transformation")
print("E[Y] =", round(mean_Y, 6)) # approx
print("Var[Y] =", round(var_Y, 6)) # approx

