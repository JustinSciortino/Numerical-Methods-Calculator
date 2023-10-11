from sympy import symbols, exp, integrate

# Define the symbol x
x = symbols('x')

# Define the function to integrate
equation = x**2 / (x**3 - exp(-x))

# Given values
a = 1
b = 3
absolute_error = 1e-8

# Calculate the true value of the integral (calculated using a symbolic solver)
true_value = integrate(equation, (x, a, b))

# Function to calculate the composite Simpson's 1/3 rule approximation
def composite_simpsons_1_3(func, a, b, m):
    h = (b - a) / (2 * m)
    x_values = [a + i * h for i in range(2 * m + 1)]
    sum_even = sum(func.subs(x, x_values[i]) for i in range(2, 2 * m, 2))
    sum_odd = sum(func.subs(x, x_values[i]) for i in range(1, 2 * m, 2))
    integral_approx = (h / 3) * (func.subs(x, a) + 4 * sum_odd + 2 * sum_even + func.subs(x, b))
    return integral_approx

# Calculate the step size (h) for the desired absolute error
h = (12 * absolute_error / ((b - a) ** 4)) ** 0.25  # Corrected calculation

# Calculate the number of sub-divisions (m)
m = int((b - a) / (2 * h))

# Calculate the approximation using the composite Simpson 1/3 rule
approximation = composite_simpsons_1_3(equation, a, b, m)

# Print the results
print(f"The step size (h) for the desired absolute error of {absolute_error} is approximately {h:.15f}")
print(f"The number of sub-divisions (m) required is approximately {m}")
print(f"The approximation using the composite Simpson 1/3 rule for m={m} is approximately {approximation:.13f}")


