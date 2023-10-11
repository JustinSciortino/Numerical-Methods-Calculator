from sympy import symbols, exp, sin, cos, ln
x = symbols('x')

"""
Question of the form: Approximate the following defined integral using the composite trapezoid rule with 𝑚=4
 sub-intervals
𝐼=∫0111+𝑥𝑑𝑥
Use 16 digits in your calculations and provide the answer with 5 significant figures."""

a = 0
b = 1
m = 4
equation = 1/(1+x)
significant_digits = 5

import sympy as sp


def Trapezoid_Rule_Comp(a, b, m, equ, significant_digits):

    h = (b - a) / m
    xi_list = [a + i * h for i in range(m + 1)]

    sum_terms = sum(equ.subs(x, xi) for xi in xi_list[1:-1])
    integral_approximation = (h / 2) * (equ.subs(x, a) + 2 * sum_terms + equ.subs(x, b))

    return integral_approximation.evalf(significant_digits)


I = Trapezoid_Rule_Comp(a, b, m, equation, significant_digits)
print("The value of the integral is: ", I)