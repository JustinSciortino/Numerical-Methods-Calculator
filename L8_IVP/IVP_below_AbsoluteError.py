"""Solve this question:
Make sure that the solution incorporates reusability and modularity

Consider the following initial value problem

𝑑𝑦/𝑑𝑡=(1−𝑡)𝑦+sin(𝑦)

with 𝑦(−1)=0.5

We want to find y(2) with an absolute error below 10−8

Use the RK4 method

Solution:
We solve the initial value problem on the interval \([-1, 2]\) for different step sizes \(h\) and we estimate
the errors using the Richardson error formula.we can conclude that, for example, a step size of \(h=10^{-3}\) will
guarantee us to give an answer with an absoluteerror below \(10^{-8}\).Solving the IVP with this step size with the
classical RK4 method yields to y(2)=2.660913870544215
"""
import numpy as np


def runge_kutta_4(f, t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + h / 2, y + k1 / 2)
    k3 = h * f(t + h / 2, y + k2 / 2)
    k4 = h * f(t + h, y + k3)

    y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y_next


def f(t, y):
    return (1 - t) * y + np.sin(y)


def adaptive_rk4_solve(f, t0, y0, t_target, abs_error):
    h = 0.1  # Initial step size
    t = t0
    y = y0

    while t < t_target:
        h = min(h, t_target - t)  # Adjust step size if needed
        y_temp = runge_kutta_4(f, t, y, h)
        error = np.abs(y_temp - runge_kutta_4(f, t + h, y_temp, h))

        if error <= abs_error:
            y = y_temp
        h = h * 0.9 * (abs_error / error) ** 0.2  # Adjust step size
        t += h

    return y


t0 = -1
y0 = 0.5
t_target = 2
abs_error = 1e-8

approximation = adaptive_rk4_solve(f, t0, y0, t_target, abs_error)

print(f"Approximation of y(2) = {approximation:.16f}")



