from sympy import symbols, cos, exp, sin, ln, sqrt
import numpy as np
x = symbols('x')

"""Question of the form: Approximate the following defined integral using the composite Simpson 1/3 rule with 𝑚=4
 sub-intervals
𝐼=∫171𝑥𝑑𝑥
Use 16 digits in your calculations and provide the answer with 5 significant figures."""

a = 0
b = 5
m = 6
equation = (5*cos(x**2))/(sqrt(x**4+5))
significant_digits = 5

def Simpson_Rule_Composite(a, b, m, equ, significant_digits):
    h = (b - a) / (2 * m)
    x1 = np.linspace(a + h, b - h, m)
    x2 = np.linspace(a + 2 * h, b - 2 * h, m - 1)

    answer = h / 3 * (equ.subs(x, a) + equ.subs(x, b) + 4 *
                 np.sum([equ.subs(x, xi) for xi in x1]) + 2 * np.sum([equ.subs(x, xi) for xi in x2]))
    return answer.evalf(significant_digits)

I = Simpson_Rule_Composite(a, b, m, equation, significant_digits)
print("The value of the integral is:", I)
