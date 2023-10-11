from sympy import integrate, symbols

x = symbols('x')

x0 = 0
x1 = 0.1
x2 = 1

a= 0
b = 1
significant_figures = 3

equation_co = ((x-x1)*(x-x2))/((x0-x2)*(x0-x1))
c0 = integrate(equation_co, (x, a, b)).evalf(significant_figures)

equation_c1 = ((x-x0)*(x-x2))/((x1-x2)*(x1-x0))
c1 = integrate(equation_c1, (x, a, b)).evalf(significant_figures)

equation_c2 = ((x-x0)*(x-x1))/((x2-x1)*(x2-x0))
c2 = integrate(equation_c2, (x, a, b)).evalf(significant_figures)

print("According to past final exam, three significant digits is enough.")
print("c0:", c0)
print("c1:", c1)
print("c2:", c2)