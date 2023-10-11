import numpy as np
import sympy as sp
from Naivegauss import NaiveGauss

#input the interpolating polynomial equation on line 41
#input the data table for arrays xi and yi
xi = np.array([0,1,2])
yi = np.array([1.5, 4, 3.4])
xCoor = 1.5 #Desired x coordinate to find the value for

#CHANGE THE INDEXES OF THE ARRAYS TO MATCH THE INTERVALS OF THE X POINTS BELOW

"""if question is like the assignment, where you are given a x point, determine the interval that x point falls in the 
xi array. Fill in the A and b matrix using the interval. B vector values represent the y values of the x interval 
coordinates

Depending on the how many x points are the intervals that is your m value. From the m value we can determine the order
of the polynomial which is m-1. 

if m = 2 -> y = ao + a1x 
   m = 3 -> y = ao + a1x + a2x^2
   
Using matrices A, a, b solve for vector a using naive gauss
"""
indexInterval1 = xi[1]
indexInterval2 = xi[2]
yValueInterval1 = yi[1]
yValueInterval2 = yi[2]
A = np.array([[1, indexInterval1], [1, indexInterval2]])
b = np.array([[yValueInterval1],[yValueInterval2]])


solution = NaiveGauss(A, b)
ao = solution[0][0]
a1 = solution[1][0]
print("ao = ",ao)
print("ai = ",a1)

#input the interpolating polynomial equation.
x = sp.Symbol('x')
equation = (ao) + (a1)*x
yValueForXcoor = equation.subs(x, xCoor)
print("y value for x = ", xCoor, ": ", yValueForXcoor)