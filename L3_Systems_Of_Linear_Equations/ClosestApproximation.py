import numpy as np
from Naivegauss import NaiveGauss

"""
Enter the A and b matrices. Enter the coordinates for the choices of the multiple choice question in the approximations.
"""

A = np.array([[5, 4, -2], [-6, 0, 1], [-2, -3, 2]])
b = np.array([[15], [1], [-6]])

approximations1 = np.array([1.1, 7, 6.5])
approximations2 = np.array([0.3, 4.9, 12.5])
approximations3 = np.array([3.1, 2.9, 7.5])
approximations4 = np.array([0.5, 7.5, 5.5])




approx_list = [approximations1, approximations2, approximations3, approximations4]

r = NaiveGauss(A, b)
print("Solution r: \n", r)
inf_norm_r = np.linalg.norm(r, ord=np.inf)
print("Answer is the lowest norm of the approximations below:")

for i in approx_list:
    inf_norm_approx = np.linalg.norm(i, ord=np.inf)
    answer = abs(inf_norm_approx - inf_norm_r)
    print(i, "      norm:     ", answer)



