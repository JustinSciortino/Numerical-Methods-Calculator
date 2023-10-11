import numpy as np

# Input data points for interpolation
xi = np.array([1,2,3,4])
yi = np.array([-5.7, 3.3, 23.1, 26.1])




def divided_differences(xi, yi):
    n = len(xi)
    F = np.zeros((n, n))
    F[:, 0] = yi

    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (xi[i+j] - xi[i])

    return F[0, :]

coefficients = divided_differences(xi, yi)

print("ON MIDTERM INCLUDE 4 DIGITS AFTER DECIMAL POINT")
print("bo: ", coefficients[0])
print("b1: ", coefficients[1])
print("b2: ", coefficients[2])
print("b3: ", coefficients[3])


