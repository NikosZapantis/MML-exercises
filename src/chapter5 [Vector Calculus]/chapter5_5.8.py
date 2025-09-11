import sympy as sp

#! Sources: [https://omz-software.com/pythonista/sympy/modules/mpmath/functions/hyperbolic.html] FOR HYPERBOLIC TANGENT

print("\n~ 5.8 Derivatives\n")

#? a) Chain rule for f(z) = exp(-1/2*z), z = y^T * S^-1 * y , y = x - m
n = 3
x = sp.Matrix(sp.symbols(f'x0:{n}')) # x e R^R
m = sp.Matrix(sp.symbols(f'm0:{n}')) # m e R^D
S = sp.MatrixSymbol('S', n, n) # S e R^DxD

y = x - m
S_inv = sp.MatrixSymbol('S_inv', n, n)
z = (y.T * S_inv * y)[0] # z e R (scalar)

f_a = sp.exp(-0.5 * z)
df_dz = sp.diff(f_a, z)
dz_dy = sp.Matrix([sp.diff(z, yi) for yi in y])
dy_dx = sp.eye(n)

df_dx_a = df_dz * dz_dy.T * dy_dx
df_dx_a = sp.simplify(df_dx_a)

print("\n~ Results for a)\n")
print("f(x) =", f_a)
print("df/dx (1 x n) =", df_dx_a)

#? b) Gradient of f(x) = tr(xx^T + σ^2*I)
s = sp.symbols('s')
x_b = sp.Matrix(sp.symbols(f'x0:{n}')) # x e R^D

f_b = sp.trace(x_b * x_b.T + s**2 * sp.eye(n))
df_dx_b = sp.Matrix([sp.diff(f_b, xi) for xi in x_b])

print("\n~ Results for b)\n")
print("f(x) =", f_b)
print("df/dx (n x 1) =", df_dx_b)

#? c) Chain rule for f = tanh(z), z = Ax + b [hyperbolic tangent with chat help (didn't find it on mml-book)]
M, N = 3, 2
x_c = sp.Matrix(sp.symbols(f'x0:{N}')) # x e R^N
A = sp.MatrixSymbol('A', M, N) # A e R^{M x N}
b = sp.Matrix(sp.symbols(f'b0:{M}')) # b e R^M
z_c = sp.Matrix(A * x_c + b)

f_c = sp.tanh(z_c)
df_dz_c = sp.diag(*[1 - sp.tanh(zi)**2 for zi in z_c])
df_dx_c = df_dz_c * A

print("f(x) =", f_c)
print("df/dx (M x N) =", df_dx_c)
