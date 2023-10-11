import numpy as np

#using LU decomposition calculator to find L and U
#https://www.emathhelp.net/en/calculators/linear-algebra/lu-decomposition-calculator/?i=%5B%5B3%2C-2%2C4%2C3%5D%2C%5B-12%2C7%2C-11%2C-24%5D%2C%5B-6%2C2%2C9%2C-44%5D%5D
#Website will give you two matrices, the L and U matrices. Input them into the code below but for the U matrix,
#it will be in the form of a 3x4 matrix. Ignore the last column and for the b vector input the values directly from the
#question and not from the removed column of U.

L = np.array([[1,0,0],[0,1,0],[8,1,1]])
U = np.array([[3, -2, 4], [0, -1, 5], [0, 0, 7]])
b = np.array([47, 37, 455])





d = np.linalg.solve(L, b)
x = np.linalg.solve(U, d)

print("Solution vector d:", d)
print("Solution vector x:", x)



