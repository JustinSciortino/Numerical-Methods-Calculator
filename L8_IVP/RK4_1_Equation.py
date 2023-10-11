"""Solve the following question:
Compute an approximation of 𝑦(4) the solution in 𝑡=4 of the following ordinary differential equation

𝑑𝑦/𝑑𝑡=𝑡**3/𝑦**2

with 𝑦(0)=1 using the classical RK4 method with ℎ=0.5

Use 16 significant figures in your calculations and give your answer with at least 6 significant figures
"""

import numpy as np

def classical_rk4_method(f, t0, y0, h, t_target):
    n = int((t_target - t0) / h)
    t_values = np.linspace(t0, t_target, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(1, n+1):
        k1 = h * f(t_values[i-1], y_values[i-1])
        k2 = h * f(t_values[i-1] + h/2, y_values[i-1] + k1/2)
        k3 = h * f(t_values[i-1] + h/2, y_values[i-1] + k2/2)
        k4 = h * f(t_values[i-1] + h, y_values[i-1] + k3)
        y_values[i] = y_values[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return y_values[-1]

def f(t, y):
    return t**3 / y**2

t0 = 0
y0 = 1
t_target = 4
h = 0.5

approximation = classical_rk4_method(f, t0, y0, h, t_target)

print(f"Approximation of y(4) = {approximation:.10f}")
