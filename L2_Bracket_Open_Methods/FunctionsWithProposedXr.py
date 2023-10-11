from sympy import symbols, exp, cos, ln, sin
x = symbols('x')

#Provide the equations into the functions list. The equations must be wrapped with brackets (). Seperate each equation
#with a comma. Provide the tolerance as well.

# Define the given functions and their corresponding xr values
functions = [
    (exp(x) + 2 ** (-x) + 2 * cos(x) - 6, 1.82938543),

    ((x - 2) ** 2 - ln(x), 3.0571034),

    (x - 0.5 * (sin(x) + cos(x)), 0.72287),

    (3 * x ** 2 - exp(x), 0.91091849),

    (ln(x - 1) + cos(x - 1), 1.3977486157)
]
tolerance = 1e-5



selected_functions = []
for func, xr in functions:
    f_xr = func.subs(x, xr)
    f_prime_xr = func.diff(x).subs(x, xr)
    relative_error = abs(f_xr / (f_prime_xr * xr))

    if relative_error < tolerance:
        selected_functions.append((func, xr))

# Display the selected functions and their xr values
for func, xr in selected_functions:
    print(f"Function: {func}")
    print(f"xr: {xr}")
    print("---")
