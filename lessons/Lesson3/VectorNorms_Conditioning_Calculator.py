import numpy as np

#Change only the matrixA. No need to touch the p variable.
matrixA = np.array([[2, -5, 4], [-1, 2.6 ,2], [5, -3, 9]])
p = 1





def calculateConditional():
    inverseA = np.linalg.inv(matrixA)
    condA = np.linalg.norm(matrixA, ord=np.inf) * np.linalg.norm(inverseA, ord=np.inf)
    return condA
def errorMagnificationFactor():
    A_norm_inf = np.linalg.norm(matrixA, ord=np.inf)
    A_inv = np.linalg.inv(matrixA)
    A_inv_norm_inf = np.linalg.norm(A_inv, ord=np.inf)
    condition_number = A_norm_inf * A_inv_norm_inf
    return condition_number


infNormA = np.linalg.norm(matrixA, ord = np.inf)
p_norm = np.power(np.sum(np.power(np.abs(matrixA), p)), 1/p)
euclideanNormA = np.linalg.norm(matrixA, ord = 2)


print("Conditional of matrix A: ", calculateConditional(), "\n")
print("Infinity norm of matrix A: ", infNormA, "\n")
print("Euclidean norm of matrix A: ", euclideanNormA, "\n")
print("The p-norm of matrix A: ", p_norm, "\n")
print("The error magnification factor of matrix A (ANY OPTION EQUAL TO OR BELOW THIS NUMBER IS THE ANSWER): ", errorMagnificationFactor(), "\n")