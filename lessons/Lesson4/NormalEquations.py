import numpy as np

# Given data points
t = np.arange(81)  # Generating t values from 0 to 80
yi = np.array([
    5.998742, 5.489184, 4.70823, 3.665968, 2.655373, 2.495919, 2.626385,
    2.727673, 2.290448, 2.778988, 3.694857, 5.663741, 5.836156, 5.099449,
    5.516707, 3.394794, 2.755975, 2.528542, 2.64395, 2.675842, 2.458308,
    2.459454, 4.216891, 6.609847, 7.079128, 5.31801, 4.887436, 3.950452,
    2.523451, 2.521249, 2.839148, 2.795239, 2.417165, 3.182529, 4.689824,
    6.141408, 7.276277, 6.127465, 5.421061, 3.807898, 2.757479, 2.487522,
    2.770786, 2.638544, 2.299741, 2.77165, 4.781756, 5.981831, 6.258649,
    5.752484, 4.88695, 3.850196, 3.052619, 2.829239, 2.977443, 2.859368,
    2.508237, 2.977709, 3.832118, 5.660625, 6.478218, 5.985629, 5.020207,
    3.183932, 2.815266, 2.778931, 2.824942, 2.954725, 2.479892, 2.614646,
    4.054531, 5.847935, 8.158388, 6.276073, 5.365104, 3.638044, 2.67007,
    2.652708, 2.885442, 2.836384, 2.548769
])

desiredValue = 1.5

# Coefficients of the model
a0 = 1
a1 = 1
a2 = 1

equ1 = a0
equ2 = a1 * np.sin((2*np.pi*t)/12)
equ3 = a2 * np.cos((2*np.pi*t)/12)

# Coefficients matrix
A = np.column_stack((np.ones_like(t, dtype=float), equ2, equ3))


coefficients = np.linalg.lstsq(A, yi, rcond=None)[0]
a0_value = coefficients[0]
a1_value = coefficients[1]
a2_value = coefficients[2]

# Calculate the predicted values
y_pred = a0_value + (a1_value * np.sin((2*np.pi*t)/12)) + (a2_value * np.cos((2*np.pi*t)/12))
residuals = yi - y_pred
RMSE = np.linalg.norm(residuals) / np.sqrt(len(t))


print("Coefficients:")
print(f"a0 = {a0_value:.16f}")
print(f"a1 = {a1_value:.16f}")
print(f"a2 = {a2_value:.16f}")
print(f"RMSE = {RMSE:.16f}")
