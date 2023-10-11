import numpy as np

#Input the following data sets and value from the question
x = np.array([1.0, 2.0, 4.0])
y = np.array([7.7,-0.2,-37])
xCoor = 3 # Interpolate for x = xCoor


n = len(x)
V = np.vander(x, increasing=True)
coefficients = np.linalg.solve(V, y)

print("a0 = ", coefficients[0])
print("a1 = ", coefficients[1])
print("a2 = ", coefficients[2])

def vandermonde_interpolation(x, coefficients):
    n = len(coefficients)
    result = 0
    for i in range(n):
        result += coefficients[i] * (x ** i)
    return result


interpolated_value = vandermonde_interpolation(xCoor, coefficients)
print("Interpolated value at x =",xCoor,": ", interpolated_value)

