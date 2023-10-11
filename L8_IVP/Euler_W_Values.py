import math

def f(t, y):
    return -3.8* math.cos(t)

def euler_method(y0, t0, t_f, h, steps):
    y = y0
    t = t0
    counter = t0
    for i in range(steps):
        print(f"w_{i} = {y:.16f}")
        y = y + h * f(t, y)
        t = t + h
        counter += h
        if counter > t_f:
            break

y0 = 4.18
t0 = 0.02
t_final = 4
h = 0.1
steps = 6  # Number of W values - 1 that will be printed if no t_final is provided (the boundary of interval)

euler_method(y0, t0, t_final, h, steps)

