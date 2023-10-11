import math
from sympy import sin

#Input the following values below from the question
x = [-2,1,3]
y = [2,-1,1]
ao = 2.5
aOne = -1.3


sum = 0
for i in range(len(x)):
    sum+= (ao + (aOne * sin(x[i])) - y[i])**2

print("SE: ", sum.evalf(16))
print("RMSE: ", math.sqrt(sum)/(math.sqrt(len(x))))

