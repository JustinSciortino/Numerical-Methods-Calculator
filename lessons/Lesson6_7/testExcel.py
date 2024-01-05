import numpy as np

def euler_method(f_x, f_y, x0, y0, t0, h, t_final):
    n = int((t_final - t0) / h) + 1
    x = x0
    y = y0
    t = t0

    for _ in range(n):
        x_new = x + h * f_x(t, x, y)
        y_new = y + h * f_y(t, x, y)
        x = x_new
        y = y_new
        t += h

    return x, y

# Define the system of differential equations
def f_x(t, x, y):
    return x * (-x - 2*y + 5)

def f_y(t, x, y):
    return y * (-x - y + 10)

# Define initial conditions
x0 = 3
y0 = 2
t0 = 4.5
h = 3.0  # One step to reach t = 4
t_final = 4

# Solve using Euler's method
x_approximation, y_approximation = euler_method(f_x, f_y, x0, y0, t0, h, t_final)

# Format and print the approximations
formatted_x_result = np.format_float_positional(x_approximation, precision=16, unique=False, fractional=False, trim='k')
formatted_y_result = np.format_float_positional(y_approximation, precision=16, unique=False, fractional=False, trim='k')
print(f"Approximation of x({t_final}) =", formatted_x_result)
print(f"Approximation of y({t_final}) =", formatted_y_result)
