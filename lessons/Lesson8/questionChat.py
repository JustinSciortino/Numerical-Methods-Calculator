"""
I need you to solve the following problem given the question, answer, graph and my code. Based on
the coordinates of the log log plot, What I need you to do is
find the h starting value that is being used to solve this problem and how much the h value is being decrimented by.
If you have questions or need clarifications ask them before you solve the problem

Question:
We want to approximate the following integral using the composite Simpson 1/3 rule:
I = integral from 1 to 2 of (e^x)-1/sin(x) dx
Which step sizes h are in the range where the error of the composite Simpson 1/3 rule is essentially only due to
truncation error?


Answer:
10^-4 and 10^-3 and 10^-2

We compute the approximation of I for various number m of sub-intervals.
Using Richardson's error formula we can estimate the absolute error and plot it in function of h = b-a/2m.
From this figure one can read for which step sizes the total error is mainly due to the truncation error

Points:
(between 10^-1 and 10^0, between 10^0 and 10^1)
(between 10^-1 and 10^0, between 10^0 and 10^-1)
(between 10^-1 and 10^-2, around 10^-1)
(around 10^-2, around 10^-2)
(between 10^-2 and 10^-3, between 10^-3 and 10^-4)
(between 10^-3 and 10^-4, between 10^-4 and 10^-5)
(around 10^-4, around 10^-6)
(between 10^-5 and 10^-4, around 10^-7)
(around 10^-5, around 10^-8)

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
    return  (1 + np.square(y))/2  # Using np.square(y) instead of y ** 2

t0 = 0
y0 = 1
t_target = 1
h = 0.5

approximation = trapezoid_rk2_method(f, t0, y0, h, t_target)
formatted_result = np.format_float_positional(approximation, precision=6, unique=False, fractional=False, trim='k')
print(f"Approximation of y(7) =", formatted_result)

