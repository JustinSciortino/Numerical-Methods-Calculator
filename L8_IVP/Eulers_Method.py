"""Solve the following question:
Consider the following initial value problem:

𝑑𝑦/𝑑𝑡=𝑡^3/𝑦^2

with 𝑦(0)=1

Apply Euler's method with a step size ℎ=0.25

How much is the approximation of 𝑦(1)?

Use 16 significant figures in your calculations and give your answer with at least 5 significant figures
"""
import numpy as np

def euler_method(f, y0,t0,h, t_final):
    n = int(t_final / h)
    t = t0
    y = y0

    for _ in range(n):
        y = y + h * f(t, y)
        t += h

    return y

# Define the differential equation
def f(t, y):
    return t**3/y**2

# Define initial conditions
y0 = 1
t0 = 0
h = 0.25
t_final = 1

# Solve using Euler's method
approximation = euler_method(f, y0,t0, h, t_final)

# Format and print the approximation of y(1) with 5 significant digits
formatted_result = np.format_float_positional(approximation, precision=14, unique=False, fractional=False, trim='k')
print(f"Approximation of y(", t_final,") = ", formatted_result)
