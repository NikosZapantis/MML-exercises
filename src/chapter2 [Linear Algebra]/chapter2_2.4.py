import numpy as np

print("~ 2.4 Computing Matrices ~")

def compute_matrices(q, An, Bn):
    A, B = matrices[An], matrices[Bn]
    print(f"\n{q}) {An} @ {Bn}")
    try:
        res = A @ B
        print(res)
    except ValueError as e:
        #! In case matrix dimensions do not match NumPy throws ValueError
        print("Not possible compute.", e)
    
# Defining matrices for each case
matrices = {
    #? a)
    "Mata1" : np.array([[1, 2],
                 [4, 5],
                 [7, 8]]),

    # This matrix is used in a), b) and c)
    "Matabc2" : np.array([[1, 1, 0],
                    [0, 1, 1],
                    [1, 0, 1]]),

    #? b)
    "Matb1" : np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]),

    #? d)
    "Matd1" : np.array([[1, 2, 1, 2],
                    [4, 1, -1, -4]]),

    "Matd2" : np.array([[0, 3],
                    [1, -1],
                    [2, 1],
                    [5, 2]])
}

# Calling def for each question
compute_matrices("a", "Mata1", "Matabc2")
compute_matrices("b", "Matb1", "Matabc2")
compute_matrices("c", "Matabc2", "Matb1")
compute_matrices("d", "Matd1", "Matd2")
compute_matrices("e", "Matd2", "Matd1")
