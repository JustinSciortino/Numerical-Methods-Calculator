"""
Equation of the form:

P2(x) = y1((x-2)(x+3) / A) + y2((x+3)(x-4) / B) + y3((x-4)(x-2) / C)

where and calculating the denominators, A, B, and C:
    x1 = 2
    x2 = -3
    x3 = 4
"""

#Enter the x values below only.
x1 = 2
x2 = -3
x3 = 4



A = (x3-x1)*(x3-x2)
B = (x1-x2)*(x1-x3)
C = (x2-x1)*(x2-x3)
print("A = ", A)
print("B = ", B)
print("C = ", C)