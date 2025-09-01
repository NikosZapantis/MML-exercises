import numpy as np

print("~ 2.5 Solving Linear Systems Ax = b ~")

# Defining systems A and b
sys = {
    "a": {
        "A": np.array([[1, 1, -1, -1],
                       [2, 5, -7, -5],
                       [2, -1, 1, 3],
                       [5, 2, -4, 2]]),
        "b": np.array([1, -2, 4, 6])
    },

    "b": {
        "A": np.array([[1, -1, 0, 0, 1],
                       [1,  1, 0, -3, 0],
                       [2, -1, 0, 1, -1],
                       [-1, 2, 0, -2, -1]]),
        "b": np.array([3, 6, 5, -1])
    },
}

#TODO: Print the S of all solutions

#! Sources used [https://numpy.org/doc/2.2/reference/routines.linalg.html] in which documenation of numpy has both .solve and .lstsq
def system_sol(q, An, bn):
    print(f"\n{q}): A shape={An.shape}, b shape={bn.shape}")

    # Checking if is square and non-singular
    if An.shape[0] == An.shape[1]:
        try:
            res = np.linalg.solve(An, bn)
            print("Unique solution:")
            print(res)
        except np.linalg.LinAlgError as e:
            #! In case matrix is singular NumPy throws LinAlgError
            print("No unique solution (matrix singular).", e)
    
    # If not square, using lstsq to find least-squares solution
    res, residuals, rank, s = np.linalg.lstsq(An, bn, rcond=None)
    print("Solution (least-squares):")
    print(res)
    if residuals.size > 0:
        print("Residuals:", residuals)

# Calling def for each question
for key, data in sys.items():
    system_sol(key, data["A"], data["b"])
