import numpy as np

#! Sources: [https://numpy.org/doc/stable/reference/constants.html / https://numpy.org/doc/stable/reference/routines.math.html]

x1 = np.array([2., 3.])
x2 = np.array([0., -1.])

# Angle (30 deg)
theta = np.pi / 6

# Rotation matrix
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])

# Rotated vectors
x1_rot = R @ x1
x2_rot = R @ x2

# Displaying results
print("\n~ 3.10 Rotation by 30 degrees")
print("\nRotation matrix R =\n", R)
print()

print("Original vector x1 =", x1)
print("Rotated vector x1 =", x1_rot)
print()

print("Original vector x2 =", x2)
print("Rotated vector x2 =", x2_rot)

# Check length after rotation [it has to be the same]
print("\nChecks:")
print("||x1|| =", np.linalg.norm(x1), "||x1'|| =", np.linalg.norm(x1_rot))
print("||x2|| =", np.linalg.norm(x2), "||x2'|| =", np.linalg.norm(x2_rot))
