import numpy as np

# Enter the data sets
xi = np.array([-2, 0, 1, 2, 3])
yi = np.array([-0.5, 1, 0.5, 0.1, 0.05])


# Linearize the model: 1/y = a0 + a1*x + a2*x^2
linearized_y = 1 / yi

# Build the coefficient matrix A
A = np.column_stack((np.ones(len(xi)), xi, xi**2))
a = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, linearized_y))

# Extract the coefficients a0 and a1
ao, a1 , a2 = a[0], a[1], a[2]

# Calculate the predicted values y_pred using the original model
y_pred = 1 / (ao + a1 * xi + a2 * xi**2)
residuals = y_pred - yi
RMSE = np.linalg.norm(residuals, 2) / np.sqrt(len(xi))

print("a0 =", ao)
print("a1 =", a1)
print("a2 =", a2)
print("Root Mean Square Error (RMSE) =", RMSE)

