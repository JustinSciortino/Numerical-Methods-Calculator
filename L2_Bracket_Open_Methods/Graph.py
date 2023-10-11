import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import symbols, solve

# Define the function
x = symbols('x')
equation = x**3 - 2*x**2 - 5*x + 6

# Find the x-axis crossings
crossings = solve(equation, x)

# Generate x and y data points for plotting
x_vals = np.linspace(-10, 10, 500)  # Adjust the range and density as needed
y_vals = [equation.subs(x, val) for val in x_vals]

# Create a pandas DataFrame to store the x and y data
df = pd.DataFrame({'x': x_vals, 'y': y_vals})

# Plot the function
plt.plot(df['x'], df['y'])
plt.axhline(y=0, color='r', linestyle='--')  # Plotting the x-axis

# Mark the x-axis crossings
for crossing in crossings:
    plt.plot(crossing, 0, 'ro')

# Set x-axis label
plt.xlabel('x')
print(crossing)
# Show the plot
plt.show()
