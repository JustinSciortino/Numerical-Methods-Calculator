from sympy import symbols, diff, ln, factorial
import numpy as np
x = symbols('x')

#Enter the values only for xi, yi that are giving in the question. Enter the equation of the function in the variable
# function. Enter the value you want to interpolate to in the variable named value.

xi = [1, 4, 6]
yi = [0, 1.386294, 1.791759]
function = ln(x)
value = 1.5

intervalToFindMaxY = (xi[0], xi[-1])
m = len(xi)

derivativeToOrderM = function.diff(x, m)

x_values = np.linspace(intervalToFindMaxY[0], intervalToFindMaxY[1], 1000)
y_values = [derivativeToOrderM.subs(x, xi) for xi in x_values]
max_y_value = max(y_values)

print(m, "rd Order Derivative of the function:", derivativeToOrderM)
print("Maximum y-value in the interval:", max_y_value)

interpolatingErrorEquation = (max_y_value/factorial(m))*(x-xi[0])*(x-xi[1])*(x-xi[2])
estimatingInterpolationError = interpolatingErrorEquation.subs(x, value)
print("The estimate of the interpolation error at x =",value, "is: ", estimatingInterpolationError)

