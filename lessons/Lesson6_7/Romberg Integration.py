from sympy import exp, sin, cos, pi, symbols, sqrt, ln
x = symbols('x')


equation = 1/(sqrt((x**2)+4))
a = 0
b = 2*(sqrt(3))
significant_digits = 9
n = 4 #number of iterations/rows

def romberg_integration_trapezoidal(func, a, b, n):
    R = {}

    h = (b - a)
    x_values = [a, b]
    R[(1, 1)] = h / 2 * (func.subs(x, x_values[0]) + func.subs(x, x_values[1]))

    for j in range(2, n + 1):
        h /= 2
        subtotal = 0

        for k in range(1, 2**(j - 2) + 1):
            subtotal += func.subs(x, a + (2 * k - 1) * h)

        R[(j, 1)] = 0.5 * R[(j - 1, 1)] + h * subtotal

    for i in range(2, n + 1):
        for j in range(2, i + 1):
            R[(i, j)] = (4**(j - 1) * R[(i, j - 1)] - R[(i - 1, j - 1)]) / (4**(j - 1) - 1)

    return R



romberg_results = romberg_integration_trapezoidal(equation, a, b, n)


romberg_dict = {}
for i in range(1, n + 1):
    for j in range(1, i + 1):
        key = f"R{i}{j}"
        romberg_dict[key] = (romberg_results[(i, j)]).evalf(significant_digits)

for i in romberg_dict:
    print(i,":", romberg_dict[i])
