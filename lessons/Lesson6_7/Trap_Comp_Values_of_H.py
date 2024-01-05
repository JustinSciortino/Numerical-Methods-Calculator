import matplotlib.pyplot as plt
from sympy import symbols, cos, exp, sin, ln, sqrt, pi
import numpy as np

a = 0
b = np.pi
q = 2
equation = lambda x: np.cos(np.exp(x))

def Richardson_Error(q, h1, h2, I_h1, I_h2):
    Error = abs((I_h2 - I_h1)/((h1/h2)**q-1))
    return Error

m_values = [1] + [2 ** i for i in range(1, 25)]  # Powers of 2 for m values
significant_digits = 10

h_I_list = []
points_dict = {}

for m in m_values:
    h = (b - a) / ( m)
    xi_list = np.linspace(a, b, m + 1)

    sum_terms = np.sum(equation(xi_list[1:-1]))
    integral_approximation = (h / 2) * (equation(a) + 2 * sum_terms + equation(b))

    h_I_list.append([h, integral_approximation])

for h_I in h_I_list:
    print(h_I)


for i in range(len(h_I_list) - 1):
    points_dict[h_I_list[i+1][0]] = Richardson_Error(q, h_I_list[i][0], h_I_list[i+1][0], h_I_list[i][1], h_I_list[i+1][1])
print(points_dict)

x_values = np.array(list(points_dict.keys()))
y_values = np.array(list(points_dict.values()))

plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')

plt.scatter(x_values, y_values, marker='o', color='b', alpha=0.7)
plt.xlim(1e-5, 1)
x_ticks = np.logspace(-8, 0, 9)  # Adjust x axis range
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