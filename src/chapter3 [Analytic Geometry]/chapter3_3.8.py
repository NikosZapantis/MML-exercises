import numpy as np

#! Sources: [https://numpy.org/doc/stable/reference/generated/numpy.dot.html]

b1 = np.array([1., 1., 1.])
b2 = np.array([-1., 2., 0.])

# Gram-Schmidt
u1 = b1.copy()
norm_u1 = np.linalg.norm(u1)
c1 = u1 / norm_u1

proj_b2_on_u1 = (np.dot(b2, u1) / np.dot(u1, u1)) * u1
u2 = b2 - proj_b2_on_u1
norm_u2 = np.linalg.norm(u2)
c2 = u2 / norm_u2

# Checks for orthonormality
dot_c1_c2 = np.dot(c1, c2)
norm_c1 = np.linalg.norm(c1)
norm_c2 = np.linalg.norm(c2)

# Displaying results
print("\n~ 3.8 Gram-Schmidt Process")
print("\nb1 =", b1)
print("b2 =", b2)
print()

print("\nu1 = b1 =", u1)
print(f"||u1|| = {norm_u1:.12f}")
print("c1 = u1 / ||u1|| =", c1)
print()

print("\nProjection of b2 on u1 =", proj_b2_on_u1)
print("u2 = b2 - proj_b2_on_u1 =", u2)
print(f"||u2|| = {norm_u2:.12f}")
print("c2 = u2 / ||u2|| =", c2)
print()

print("\nChecks: <c1, c2> =", dot_c1_c2)
print("||c1|| =", norm_c1, "||c2|| =", norm_c2, "(they should be 1)")
