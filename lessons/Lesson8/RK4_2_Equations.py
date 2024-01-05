"""Solve the following question using numpy:
Apply the standard RK4 method to the following initial value problem:

𝑑2𝑦/𝑑𝑡2 − 2*𝑑𝑦/𝑑𝑡 + 2*𝑦= 𝑒^(2𝑡) * sin(𝑡)
𝑦(0)=−0.4
𝑦′(0)=−0.6

with a step size of ℎ=0.25 in the interval [0,1]

Start by transforming this second order differential equation into a system of first order differential equations by using the variables

𝑦1=𝑦
𝑦2=𝑑𝑦𝑑𝑡

Give the approximations 𝑤1 and 𝑤2 of 𝑦1 and 𝑦2 in 𝑡=1
Use 16 digits in your calculations and give the answers with at least 5 significant digits

𝑤1(1)=
𝑤2(1)="""
import numpy as np

def f(t, y):
    y1, y2 = y
    return np.array([y2, 2 * y2 - 2 * y1 + np.exp(2 * t) * np.sin(t)])

def rk4_step(f, t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + h / 2, y + k1 / 2)
    k3 = h * f(t + h / 2, y + k2 / 2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

t0 = 0
y0 = np.array([-0.4, -0.6])
h = 0.25
n = int((1 - t0) / h)

t = t0
y = y0

for _ in range(n):
    y = rk4_step(f, t, y, h)
    t += h

w1 = y[0]
w2 = y[1]

print(f"w1(1) = {w1:.14f}")
print(f"w2(1) = {w2:.14f}")
