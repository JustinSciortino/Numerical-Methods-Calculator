"""
There is a problem with this code. I need you to look at the question below and
fix the error in the code.
Question:
Apply the standard RK4 method to the following initial value problem:
t^2 * y'' - 2t * y' + 2y = t^3 * ln(t)
y(1) = 1
y'(1) = 0

with a step size of h = 0.25 in the interval [1,2]
Start by transforming this second order differential equation into a system of first order differential equations by
using the variables
y1 = y
y2 = dy/dt

Give the approximations w1 and w2 of y1 and y2 in t = 2.
Use 16 digits in your calculations and give the answers with at least 5 significant digits
"""

#The function f needs to be modified by inputing the equation. The code on lines 37-40 need to be modified as well.

import numpy as np

def f(t, y):
    y1, y2 = y
    #In the below array, do not touch the y2 element and input your equation after the comma
    #When inputting the equation, first transform the equation so that there is no coefficients in front of the y'' term
    return np.array([y2, 2/t * y2 - 2/t**2 * y1 + t * np.log(t)])

def rk4_step(f, t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + h / 2, y + k1 / 2)
    k3 = h * f(t + h / 2, y + k2 / 2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

t0 = 1 #initial value of t, number in y(1) and y'(1)
t_desired = 2
y0 = np.array([1, 0]) #value of y(1) and y'(1)
h = 0.25
n = int((t_desired - t0) / h)

t = t0
y = y0

for _ in range(n):
    y = rk4_step(f, t, y, h)
    t += h

#Do not touch the below code
w1 = y[0]  # Index 0 corresponds to y1 (w1)
w2 = y[1]   # Index 1 corresponds to y2 (w2)

print(f"w1(2) = {w1:.14f}")
print(f"w2(2) = {w2:.14f}")

