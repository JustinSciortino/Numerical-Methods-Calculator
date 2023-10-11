import numpy as np

#Input
matrixA = np.array([[2, -5,4], [-1, 2.6, 2], [5, -3, 9]])
matrixB = np.array([[29],[-10], [-32]])
matrixXR = np.array([[3.1],[10], [7.5]])
matrixR = np.linalg.solve(matrixA, matrixB)

np.set_printoptions(precision=16)

print("Matrix A:\n", matrixA, "\n")
print("Matrix B:\n", matrixB, "\n")
print("Matrix Xr:\n", matrixXR, "\n")
print("Matrix r:\n", matrixR, "\n")

inverseA = np.linalg.inv(matrixA)
print("Matrix inverse A:\n", inverseA, "\n")

def BackError():
    result = (np.dot(matrixA, matrixXR)) - matrixB
    absoluteBackError = np.linalg.norm(result, ord = np.inf)
    relativeBackError = absoluteBackError / np.linalg.norm(matrixB, ord = np.inf)
    #rounding to 2 decimal points/ 2 significant digits
    roundedrbe = np.format_float_positional(relativeBackError, precision=5, unique=False, fractional=False)
    roundAbsoluteBackError = np.format_float_positional(absoluteBackError, precision=5, unique=False, fractional=False)
    print("The relative backward error is: ",roundedrbe)
    print("The absolute backward error is: ", roundAbsoluteBackError, "\n")
    return relativeBackError


def ForwardError():
    relative_forward_error = np.linalg.norm(matrixR - matrixXR, ord=np.inf) / np.linalg.norm(matrixR, ord=np.inf)
    roundrfe = np.format_float_positional(relative_forward_error, precision=2, unique=False, fractional=False)
    absoluteForwardError = np.linalg.norm(matrixR - matrixXR, ord=np.inf)
    roundAbsoluteFE = np.format_float_positional(absoluteForwardError, precision=2, unique=False, fractional=False)
    print("The relative forward error is: ", roundrfe)
    print("The absolute forward error is: ", roundAbsoluteFE, "\n")
    return relative_forward_error

def ErrorMagnFactor():
    EMF = ForwardError()/BackError()
    print("The Error Magnification Factor M is: ", EMF, "\n")

def cond():
    condA = np.linalg.norm(matrixA, ord = np.inf) * np.linalg.norm(inverseA, ord = np.inf)
    print("Conditional of matrix A: ", condA, "\n")
    return condA

def dValue(c):
    d = np.log10(c)
    d = np.format_float_positional(d, precision=10, unique=False, fractional=False)
    print("d value/ digits lost: ", d, "\n")

ErrorMagnFactor()
condValue = cond()
dValue(condValue)