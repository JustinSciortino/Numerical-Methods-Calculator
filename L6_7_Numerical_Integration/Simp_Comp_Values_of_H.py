import matplotlib.pyplot as plt
import numpy as np

def Simpson_Rule_Composite(a, b, m, equ):
    h = (b - a) / (2 * m)
    x1 = np.linspace(a + h, b - h, m)
    x2 = np.linspace(a + 2 * h, b - 2 * h, m - 1)

    terms_x1 = equ(x1)
    terms_x2 = equ(x2)

    answer = h / 3 * (equ(a) + equ(b) + 4 * np.sum(terms_x1) + 2 * np.sum(terms_x2))
    return answer

def Richardson_Error(q, h1, h2, I_h1, I_h2):
    Error = abs((I_h2 - I_h1)/((h1/h2)**q-1))
    return Error

a = 0
b = 2
equation = lambda x: (np.exp(2*x))*(np.sin(3*x))  # Adjust the equation here

q = 4
m_values = [1] + [2**i for i in range(1, 21)]
significant_digits = 10
h_I_list = []
points_dict = {}

for m in m_values:
    h = (b - a) / (2 * m)
    I = Simpson_Rule_Composite(a, b, m, equation)
    h_I_list.append([h, I])

for i in range(len(h_I_list) - 1):
    points_dict[h_I_list[i+1][0]] = Richardson_Error(q, h_I_list[i][0], h_I_list[i+1][0], h_I_list[i][1], h_I_list[i+1][1])

x_values = np.array(list(points_dict.keys()))
y_values = np.array(list(points_dict.values()))

plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')

plt.scatter(x_values, y_values, marker='o', color='b', alpha=0.7)

plt.xlabel('h values')
plt.ylabel('Estimated Error')
plt.title('Richardson Error Analysis (Log-Log Plot)')
plt.grid(True)
plt.show()
