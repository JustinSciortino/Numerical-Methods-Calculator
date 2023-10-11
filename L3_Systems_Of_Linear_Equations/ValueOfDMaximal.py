import numpy as np


# Enter the matrix A, for the unknown d, enter np.nan
A = np.array([[-4.2, 0.7], [-12.6, np.nan]])



d = (A[1][0] / A[0][0]) * A[0][1]
A[1, 1] = d
cond_A = np.linalg.cond(A)
print("Use 3 significant digits unless otherwise stated in the question.")
print("Value of d:", d)
print("Condition number of A:", cond_A)