import numpy as np
def NaiveGauss (A, b):
    solution = np.linalg.solve(A, b)
    return solution
