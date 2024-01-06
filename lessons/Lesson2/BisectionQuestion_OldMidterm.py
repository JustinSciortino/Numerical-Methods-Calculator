import numpy as np

"""
You must enter the matrix A in the calculate_determinant function on line 11. You may have to change the value to 
subtract from the matrix in the f(x) function on line 31. You have to provide the initial interval for x in the 
initial_interval variable on line 35 and provide the tolerance on line 38.
"""

# Function to calculate the determinant of the matrix A with a given x
def calculate_determinant(x):
    A = np.array([[x, 1, 2, 3], [4, x, 5, 6], [7, 8, x, 9], [10, 11, 12, x]])
    return np.linalg.det(A)

# Bisection method function
def bisection_method(f, a, b, tolerance):
    iterations = 0
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c, iterations
        if np.sign(fc) == np.sign(f(a)):
            a = c
        else:
            b = c
        iterations += 1
    return (a + b) / 2, iterations

# Define the function f(x) = det(A(x)) - 10000
def f(x):
    return calculate_determinant(x) - 10000

# Initial interval for x with more decimal places
initial_interval = [14.050, 14.051]

# Set the tolerance (absolute error) to 10^-3
tolerance = 1e-3

# Perform bisection method to find the root
root, iterations = bisection_method(f, initial_interval[0], initial_interval[1], tolerance)

print("Root: {:.4f} (approximated to ±0.001), Iterations: {}".format(root, iterations))
