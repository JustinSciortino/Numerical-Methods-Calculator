from sympy import *
x = symbols('x')


a = 1.4
b = 4.7
equation = cos(2.9*x)*exp(-3.2*x)
significant_digits = 5

def Sympson(a , b, equ):
    h = (b-a)/2
    return (h/3)*(equ.subs(x,a) + 4*equ.subs(x,((a+b)/2)) + equ.subs(x,b))

I = Sympson(a,b,equation).evalf(significant_digits)
print("The value of the integral is: ", I)
