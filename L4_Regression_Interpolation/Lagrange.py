from sympy import symbols
x = symbols('x')

#Enter the values below from lines 5-8. Do not touch the rest of the code.
xCoor = 4.5
sf = 16
xi = [-8.7, 2.2, 6.8]
yi = [10, 3.7, 8.6]



m = len(xi)
L0 = ((x-xi[1])*(x-xi[2]))/((xi[0]-xi[1])*(xi[0]-xi[2]))
L1 = ((x-xi[0])*(x-xi[2]))/((xi[1]-xi[0])*(xi[1]-xi[2]))
L2 = ((x-xi[0])*(x-xi[1]))/((xi[2]-xi[0])*(xi[2]-xi[1]))

P = yi[0]*L0 + yi[1]*L1 + yi[2]*L2

def evaluateLagrangePolynomial(x):
    print("P at xCoor: ", P.subs('x', x).evalf(sf))

def evaluateLagrangeMonomial(x):
    print("if you get zoo as the answer it means that the answer is too large. Compute it by hand.")
    print("L0: ", L0.subs('x', x).evalf(sf))
    print("L1: ", L1.subs('x', x).evalf(sf))
    print("L2: ", L2.subs('x', x).evalf(sf))

evaluateLagrangeMonomial(xCoor)
evaluateLagrangePolynomial(xCoor)