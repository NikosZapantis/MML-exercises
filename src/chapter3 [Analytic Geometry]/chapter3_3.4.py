import numpy as np

#! Sources [https://numpy.org/doc/stable/reference/generated/numpy.arccos.html / https://numpy.org/doc/stable/reference/generated/numpy.degrees.html]

x = np.array([1, 2], dtype=float)
y = np.array([-1, -1], dtype=float)

# a) Dot product
dot_xy = x @ y
norm_x = np.linalg.norm(x)
norm_y = np.linalg.norm(y)

cos_theta = dot_xy / (norm_x * norm_y)
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

# b) With B
B = np.array([[2, 1], 
              [1, 3]], dtype=float)

dot_xy_B = x @ B @ y
norm_x_B = np.sqrt(x @ B @ x)
norm_y_B = np.sqrt(y @ B @ y)

cos_theta_B = dot_xy_B / (norm_x_B * norm_y_B)
theta_rad_B = np.arccos(cos_theta_B)
theta_deg_B = np.degrees(theta_rad_B)

# Displaying results
print("\n~ 3.4 Angle between x and y")
print(f"\na) Standard dot product: theta = {theta_rad:.12f} rad = {theta_deg:.3f}°")
print(f"\nb) With B: theta = {theta_rad_B:.12f} rad = {theta_deg_B:.3f}°")
