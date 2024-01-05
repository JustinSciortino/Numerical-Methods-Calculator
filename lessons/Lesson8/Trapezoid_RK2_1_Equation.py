"""Solve the following question using numpy and reusability and modularity:
Compute the approximation of 𝑦(7), the solution in 𝑡=7
 of the following ordinary differential equation

𝑑𝑦/𝑑𝑡=1+(𝑡−𝑦)^2

with 𝑦(2)=1 using the Trapezoid RK2 method with ℎ=0.5

Use 16 significant figures in your calculations and give your answer with at least 6 significant figures
"""
import numpy as np

def trapezoid_rk2_method(f, t0, y0, h, t_target):
    n = int((t_target - t0) / h)
    t_values = np.linspace(t0, t_target, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(1, n+1):
        k1 = h * f(t_values[i-1], y_values[i-1])
        k2 = h * f(t_values[i], y_values[i-1] + k1)
        y_values[i] = y_values[i-1] + (k1 + k2) / 2

    return y_values[-1]

def f(t, y):
    return (1+y**2)/2

t0 = 0
y0 = 1
t_target = 1
h = 0.2

approximation = trapezoid_rk2_method(f, t0, y0, h, t_target)
formatted_result = np.format_float_positional(approximation, precision=7, unique=False, fractional=False, trim='k')
print(f"Approximation of y(7) = ", formatted_result)


