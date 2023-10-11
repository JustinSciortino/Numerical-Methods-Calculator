from sympy import *
x = symbols('x')

a = 1.2
b = 6.8
equation = cos(8.9*x)*exp(x)
significant_digits = 8

def Trapezoid(a , b, equ):
    h = (b-a)
    return (h)*((equ.subs(x,a) + equ.subs(x,b))/2)

I = Trapezoid(a,b,equation).evalf(significant_digits)
print("The value of the integral is: ", I)
