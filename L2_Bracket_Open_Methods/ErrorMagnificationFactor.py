from sympy import symbols, diff, cos, exp, sin, ln, log, factorial

x = symbols('x')

#Find the value of r using desmos. Closest root to coordinate (0, 0)
#Enter the r, xr and equation below
equation = x**2-10*x+21
r = 3
xr = 3.36

M = abs(xr-r)/abs(equation.subs(x, xr))

print("The Error magnification factor is ",M, "(for midterm he used 2 decimal places but it was a MC)")