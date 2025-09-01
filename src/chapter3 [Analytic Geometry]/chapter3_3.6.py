import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#! Sources [https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html]

A = np.array([[2., 1., 0.], 
              [1., 2., -1.], 
              [0., -1., 2.]])

#? Standard/canonical basis of R^3
e1 = np.array([1., 0., 0.])
e2 = np.array([0., 1., 0.])
e3 = np.array([0., 0., 1.])

# U cols -> e1, e3
U = np.column_stack([e1, e3])
v = e2.copy()

# Calculating projection U to inner product x^T A y
M = U.T @ A @ U # 2x2
rhs = U.T @ A @ v # 2x1

# Solving M * coeffs = rhs
c = np.linalg.solve(M, rhs)
proj = U @ c # π_U(v)
residual = v - proj

# Distance
dist = np.sqrt(residual @ (A @ residual))

# Displaying results
print("\n~ 3.6 Projection & Distance")
print("\nMatrix A =\n", A)
print("\nSubscpace U = span{e1, e3}")
print("\nRight-hand vector v = e2 =", v)
print("\n(U^T A U) =\n", M)
print("\n(U^T A v) =", rhs)
print("\nCoefficients c (so that proj = c1*e1 + c2*e3):", c)
print("\nProjection π_U(e2) =", proj)
print("\nResidual (e2 - π_U(e2)) =", residual)
print("\nDistance d(e2, U) = ||e2 - π_U(e2)||_A =", f"{dist:.6f}")

#? 3D Visual
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')
origin = np.zeros(3)

# Plotting basis vectors
ax.quiver(*origin, *e1, color='r', label='e1', length=1.0, normalize=False)
ax.quiver(*origin, *e2, color='g', label='e2', length=1.0, normalize=False)
ax.quiver(*origin, *e3, color='b', label='e3', length=1.0, normalize=False)

# Plotting projection
ax.scatter(*proj, color='m', s=60, label=r'$\pi_U(e_2)$')
ax.text(*(proj + 0.05), r'$\pi_U(e_2)$', color='m')

# Arrow from e2 to its projection
ax.quiver(*v, *(proj - v), color='k', linestyle='--', linewidth=1.2, arrow_length_ratio=0.05)
ax.text(*(v + 0.05), 'e2', color='g')

# Axes and labels
ax.set_xlim([-0.6,1.1]); ax.set_ylim([-0.6,1.1]); ax.set_zlim([-0.6,1.1])
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.view_init(elev=20, azim=30)
ax.legend()
plt.title(r"Projection of $e_2$ onto $U=\mathrm{span}\{e_1,e_3\}$ w.r.t. $\langle\cdot,\cdot\rangle_A$")
plt.tight_layout()
plt.show()
