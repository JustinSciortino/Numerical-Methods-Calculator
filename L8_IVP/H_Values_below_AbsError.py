import numpy as np
import matplotlib.pyplot as plt

RK2 = False
RK4 = True

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
    return 2 * (t + 1) * y


true_solution_at_t_1 = np.exp(1**2 - 1)

t0 = 0
y0 = 1
t_target = 1
h_start = 0.1

h_values = []
approximation_list = []
q = 0

if RK2:
    q = 2
    for counter in range(18):
        approximation = trapezoid_rk2_method(f, t0, y0, h_start, t_target)
        absolute_error = abs(approximation - true_solution_at_t_1)

        if absolute_error < 1e-3:
            h_values.append(h_start)

        approximation_list.append([h_start, approximation])
        h_start /= 2
else:
    q = 4
    for counter in range(18):
        approximation = classical_rk4_method(f, t0, y0, h_start, t_target)
        absolute_error = abs(approximation - true_solution_at_t_1)

        if absolute_error < 1e-3:
            h_values.append(h_start)

        approximation_list.append([h_start, approximation])
        h_start /= 2
points_dict = {}


for i in range(len(approximation_list) - 1):
    points_dict[approximation_list[i+1][0]] = abs((approximation_list[i+1][1] - approximation_list[i][1]) / ((approximation_list[i][0]/approximation_list[i+1][0])**q - 1))

x_values = np.array(list(points_dict.keys()))
y_values = np.array(list(points_dict.values()))

plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')

plt.scatter(x_values, y_values, marker='o', color='b', alpha=0.7)
plt.xlim(1e-5, 1)
x_ticks = np.logspace(-8, 0, 9)
x_labels = [f"${x:.0e}$" for x in x_ticks]
plt.xticks(x_ticks, x_labels)

plt.ylim(1e-15, 1)
y_ticks = np.logspace(-15, 0, 16)
y_labels = [f"${y:.0e}$" for y in y_ticks]
plt.yticks(y_ticks, y_labels)

plt.xlabel('h values')
plt.ylabel('Estimated Error')
plt.title('Richardson Error Analysis (Log-Log Plot)')
plt.grid(True)
plt.show()
