"""Solve the question of the type:
Apply the Trapezoid (RK2) method to the following initial value problem:

𝑦′1=𝑦1+𝑦2
𝑦′2=−𝑦1+𝑦2
𝑦1(0)=1
𝑦2(0)=0

with a step size of ℎ=0.1 in the interval [0,1]

Give the approximations 𝑤1 and 𝑤2 of 𝑦1 and 𝑦2 in 𝑡=1

Use 16 digits in your calculations and give the answers with at least 5 significant digits

𝑤1(1)= 1.48048
𝑤2(1)= -2.28900
"""
import numpy as np

def trapezoid_rk2(f, t0, y0, h, n):
    t_values = [t0]
    y_values = [y0]

    for _ in range(n):
        t = t_values[-1]
        y = y_values[-1]

        k1 = h * f(t, y)
        k2 = h * f(t + h, y + k1)

        t_values.append(t + h)
        y_values.append(y + 0.5 * (k1 + k2))

    return t_values, y_values

# Define the system of ODEs
def f(t, y):
    y1, y2 = y
    return np.array([y1 + y2, -y1 + y2])

t0 = 0
y0 = np.array([1.0, 0.0])
h = 0.1
n = int((1 - t0) / h)  # Calculate the number of steps

t_values, y_values = trapezoid_rk2(f, t0, y0, h, n)

# Print the approximations for t = 1

print(f"w1(1) = {y_values[-1][0]:.14f}")
print(f"w2(1) = {y_values[-1][1]:.14f}")



