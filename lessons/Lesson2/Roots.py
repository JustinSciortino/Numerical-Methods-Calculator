from sympy import symbols, sin, lambdify
import pandas as pd
from scipy.optimize import root_scalar, root

x = symbols('x')

#INPUT THE EQUATIONS
equation = x**2-11*x+10

def rootNoInterval():
    equation_numeric = lambdify(x, equation)    # Convert the equation to a numerical function
    # Find the x-axis crossings numerically
    crossing_result = root(equation_numeric, x0=0)  # Find the x-axis crossings numerically
    # Starting from x = 0, adjust as needed
    crossing = crossing_result.x[0]
    print("Crossing:", crossing)

def rootInterval():
    x = symbols('x')
    equation_numeric = lambdify(x, equation)

    # INPUT THE INTERVALS
    a = 0
    b = 4

    crossing_result = root_scalar(equation_numeric, method='brentq', bracket=[a, b])
    crossing = crossing_result.root
    print("Crossing:", crossing)

rootInterval()

