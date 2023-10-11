from sympy import symbols, diff, cos, exp, sin, ln, log, factorial
import pandas as pd
from Iterations import findNumberOfIterations
x = symbols('x')

#Only lines 8-12 must be modified. Input the required equation and the initial guess bracket.

equation = (exp(x)/(x-4))+3
significantFigures = 16 #significant figures
tolerance = 1e-7   #toleranceerance value
ao = 3
bo = 5


negativeSign = "-"
positiveSign = "+"
bisectionList = []
n = findNumberOfIterations(ao, bo, tolerance) #number of iterations needed that are within the toleranceerance

def findXi(a,b):
    xi = (a+b)/2
    return xi

def inputValueIntoEquation(val):
    v = equation.subs(x, val)
    return v

for i in range(n+1):
    signOfXi = ""
    signOfBi = ""
    signOfAi = ""
    if i == 0:
        xi = findXi(ao, bo)

        if inputValueIntoEquation(ao) < 0:
            signOfAi = negativeSign
        else:
            signOfAi = positiveSign

        if inputValueIntoEquation(bo) < 0:
            signOfBi = negativeSign
        else:
            signOfBi = positiveSign

        if inputValueIntoEquation(xi) < 0:
            signOfXi = negativeSign
        else:
            signOfXi = positiveSign

        sublist = [i, ao, bo, xi, signOfAi, signOfBi, signOfXi]
        bisectionList.append(sublist)

    else:
        previousIteration = bisectionList[-1]
        if previousIteration[-3] == negativeSign and previousIteration[-1] == negativeSign:
            ai = (previousIteration[3])
            bi = (previousIteration[2])
            xi = (findXi(ai, bi))
            if inputValueIntoEquation(ai) < 0:
                signOfAi = negativeSign
            else:
                signOfAi = positiveSign

            if inputValueIntoEquation(bi) < 0:
                signOfBi = negativeSign
            else:
                signOfBi = positiveSign

            if inputValueIntoEquation(xi) < 0:
                signOfXi = negativeSign
            else:
                signOfXi = positiveSign

            sublist = [i, ai, bi, xi, signOfAi, signOfBi, signOfXi]
            bisectionList.append(sublist)

        else:
            ai = (previousIteration[1])
            bi = (previousIteration[3])
            xi = findXi(ai, bi)
            if inputValueIntoEquation(ai) < 0:
                signOfAi = negativeSign
            else:
                signOfAi = positiveSign

            if inputValueIntoEquation(bi) < 0:
                signOfBi = negativeSign
            else:
                signOfBi = positiveSign

            if inputValueIntoEquation(xi) <= 0:
                signOfXi = negativeSign
            else:
                signOfXi = positiveSign

            sublist = [i, ai, bi, xi, signOfAi, signOfBi, signOfXi]
            bisectionList.append(sublist)

def generateDiagram():
    pd.set_option('display.float_format', lambda x: f"{x:.{significantFigures}f}")
    df = pd.DataFrame(bisectionList, columns=['i', 'ai', 'bi', 'xi', 'f(ai)', 'f(bi)', 'f(xi)'])
    df.set_index('i', inplace=True)
    print(df)
    print('\n')

generateDiagram()
print("Answer: ", bisectionList[-1][-4], " +/- ", tolerance, " *WARNING MUST BE SAME NUMBER OF significantFigures OR DECIMAL DIGITS \nIe if tolerance "
                                                "== 0.005, include 3 digits so 0.449")