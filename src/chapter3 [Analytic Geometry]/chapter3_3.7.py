import numpy as np

#! Sourcs: [https://numpy.org/doc/stable/reference/generated/numpy.diag.html / https://numpy.org/doc/2.3/reference/generated/numpy.eye.html / https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html]

def nullspace(A, tol=1e-12):
    # Returns basis of nullspace as cols
    U, s, VT = np.linalg.svd(A)
    rank = (s > tol).sum()
    return VT[rank:].T

# Defining P (projection to span{e1, e2})
P = np.diag([1., 1., 0.])
I = np.eye(3)
Q = I - P # id - π

# Checks
check_P = np.allclose(P @ P, P)
check_Q = np.allclose(Q @ Q, Q)

# Image
U_p, s_p, VT_p = np.linalg.svd(P)
rank_p = (s_p > 1e-12).sum()
imP_basis = U_p[:, :rank_p] # orthogonal basis of im(P)
kerP_basis = nullspace(P) # orthogonal basis of ker(P)

# Q = I - P
U_q, s_q, VT_q = np.linalg.svd(Q)
rank_q = (s_q > 1e-12).sum()
imQ_basis = U_q[:, :rank_q] # orthogonal basis of im(Q)
kerQ_basis = nullspace(Q) # orthogonal basis of ker(Q)

# Displaying results
print("\n~ 3.7 Projection checks")
print("\nP =\n", P)
print("\nQ = I - P =\n", Q)
print("\nCheck P^2 = P:", check_P)
print("Check Q^2 = Q [(I - P)^2 = (I - P)]:", check_Q)

print()
print("\nIm(P) basis (cols):\n", imP_basis)
print("\nKer(P) basis (cols):\n", kerP_basis)

print()
print("\nIm(Q) basis (cols):\n", imQ_basis)
print("\nKer(Q) basis (cols):\n", kerQ_basis)
