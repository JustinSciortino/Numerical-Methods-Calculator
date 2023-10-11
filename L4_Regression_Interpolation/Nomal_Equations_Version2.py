import numpy as np


years = np.arange(1980, 2014)
t = years - 1980

yi = np.array([
    3776958, 3806932, 3971528, 4014410, 4245984, 4468841, 4595862, 4729977,
    4847836, 4937608, 4985198, 4899121, 4822734, 4804214, 4876643, 4963393,
    5071268, 5079188, 5036898, 4966055, 5125933, 5347692, 5447586, 5836786,
    6306562, 6735260, 7027942, 7368969, 7575696, 7625502, 8121372, 8739880,
    8888548, 8971837
])


desiredValue = 1.5

# Coefficients of the model
a0 = 1
a1 = 1
a2 = 1
a3 = 1

# Model equation using numpy functions
equ1 = a0
equ2 = a1 * t
equ3 = a2 * t**2
equ4 = a3 * t**3

# Coefficients matrix
A = np.column_stack((np.ones_like(t, dtype=float), equ2, equ3, equ4))

# Calculate the coefficients using the normal equation
coefficients = np.linalg.lstsq(A, yi, rcond=None)[0]

# Extract the coefficients
a0_value = coefficients[0]
a1_value = coefficients[1]
a2_value = coefficients[2]
a3_value = coefficients[3]

# Calculate the predicted values
y_pred = a0_value + (a1_value * t) + (a2_value * t**2)+ (a3_value * t**3)

# Calculate the residuals
residuals = yi - y_pred

# Calculate the RMSE
RMSE = np.linalg.norm(residuals) / np.sqrt(len(t))

# Display the results
print("Coefficients:")
print(f"a0 = {a0_value:.16f}")
print(f"a1 = {a1_value:.16f}")
print(f"a2 = {a2_value:.16f}")
print(f"RMSE = {RMSE:.16f}")
