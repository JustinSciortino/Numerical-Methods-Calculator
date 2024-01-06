from sympy import log, sin, cos, exp, ln
import math

#Input values
a = 0
b = 1
tolerance= 0.005


def findNumberOfIterations(ao, bo, tol):
    n = ((log(bo-ao)-log(tol))/log(2))-1
    n = math.ceil(n)
    return n
print("The number of iterations n: ", findNumberOfIterations(a, b, tolerance))