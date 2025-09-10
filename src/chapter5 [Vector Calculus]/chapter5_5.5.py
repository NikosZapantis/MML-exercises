import sympy as sp

#! Sources: [https://www.tutorialspoint.com/sympy/sympy_symbols.htm]
#! From theory I have:
#! If f: R^n -> R^m then jacobian is m x n
#! For scalar output (m = 1), gradient is 1 x n
#! For matrix output we compute jacobian for each element

print("\n~ 5.5 Dimensions [Jacobian]")
print("f1: scalar output => Jacobian 1x2 (gradient 2x1)")
print("f2: scalar output => Jacobian 1xn (gradient nx1)")
print("f3: matrix nxn output")

# Computing Jacobians and displaying results
print("\nComputing Jacobians")

#? f1(x)
x1, x2 = sp.symbols('x1 x2')
f1 = sp.sin(x1) * sp.cos(x2)
f1_jac = [sp.diff(f1, x1), sp.diff(f1, x2)]

print("\nf1(x) =", f1)
print("Jacobian (1x2) =", f1_jac)

#? f2(x)
n = 3 # dimension
x = sp.symbols('x0:%d' % n) # this creates (x0, x1, ..., x(n-1)) [https://www.tutorialspoint.com/sympy/sympy_symbols.htm]
y = sp.symbols('y0:%d' % n)
x_vec = sp.Matrix(x)
y_vec = sp.Matrix(y)
f2 = (x_vec.T * y_vec)[0]
f2_jac = [sp.diff(f2, xi) for xi in x]

print("\nf2(x,y) =", f2)
print("Jacobian (1xn) =", f2_jac)
# df2 / dx = y^T

#? f3(x)
z0, z1, z2 = sp.symbols('z0 z1 z2')
x_demo = sp.Matrix([z0, z1, z2])
f3 = x_demo * x_demo.T

print("\nf3(x) =", f3)

# Computing Jacobian for each element
for i in range(3):
    for j in range(3):
        df = sp.diff(f3[i, j], z0)
        print(f"d(f3[{i},{j}]) / dz0 =", df)

