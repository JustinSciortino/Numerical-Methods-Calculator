from sympy import symbols, exp, sin, cos, ln, sqrt, pi
import numpy as np
x = symbols('x')

a = 0
b = np.pi/2
m = 8
equation = (1 - cos(x)) / x**2
significant_digits = 5

h = (b - a) / m
x_values = np.linspace(a + h/2, b - h/2, m)
I = h * np.sum([equation.subs(x, x_i) for x_i in x_values])
print("I =", I.evalf(significant_digits))


