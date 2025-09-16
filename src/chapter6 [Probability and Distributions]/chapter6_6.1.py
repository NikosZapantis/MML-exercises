import numpy as np

#! Sources: [https://stackoverflow.com/questions/209840/make-a-dictionary-dict-from-separate-lists-of-keys-and-values]

p_xy = np.array([
    [0.01, 0.02, 0.03, 0.10, 0.10],
    [0.05, 0.10, 0.05, 0.07, 0.20],
    [0.10, 0.05, 0.03, 0.05, 0.04]
])

x_lab = ["x1", "x2", "x3", "x4", "x5"]
y_lab = ["y1", "y2", "y3"]

#? a) Marginal distributions
p_x = p_xy.sum(axis=0) # sum on rows
p_y = p_xy.sum(axis=1) # sum on cols

#? b) Conditional distributions

# p(x|Y=y1)
p_y1 = p_xy[0, :] / p_y[0]

# p(y|X=x3) [2 is the index of x3 col]
p_x3 = p_xy[:, 2] / p_x[2]

#? Rounding to 4 decimals
p_x = np.round(p_x, 4)
p_y = np.round(p_y, 4)
p_y1 = np.round(p_y1, 4)
p_x3 = np.round(p_x3, 4)

# Display results
print("\n~ 6.1 Distributions")

print("\na) Marginal distributions")
print("p(x):", dict(zip(x_lab, p_x)))
print("p(y):", dict(zip(y_lab, p_y)))

print("\nb) Conditional distribtions")
print("p(x|Y=y1):", dict(zip(x_lab, p_y1)))
print("p(y|X=x3):", dict(zip(y_lab, p_x3)))
