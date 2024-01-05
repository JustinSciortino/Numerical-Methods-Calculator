from sympy import symbols, diff, cos, exp, sin, ln, log, factorial
import pandas as pd
x = symbols('x')


#Input, must provide initial guess bracket
equation = (x**3.5)-80
significantFigures = 16 #significant figures
tolerance = 0.8   #toleranceerance value
ao = 2
bo = 5


negativeSign = "-"
positiveSign = "+"
FalsePositionList = []
def findXi(a,b):
    xi = (a*inputValueIntoEquation(b)-b*inputValueIntoEquation(a))/(inputValueIntoEquation(b)-inputValueIntoEquation(a))
    return xi

def inputValueIntoEquation(val):
    value = equation.subs(x, val)
    return value

def calculateAbsoluteError(a,b):
    error = abs((b-a)/2)
    return error

for i in range(100):
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
        error = calculateAbsoluteError(ao, bo)
        sublist = [i, ao, signOfAi, bo, signOfBi, xi, signOfXi, error]
        FalsePositionList.append(sublist)
        if error <= tolerance:
            break

    else:
        previousIteration = FalsePositionList[-1]
        if previousIteration[2] == negativeSign and previousIteration[-2] == negativeSign:
            ai = previousIteration[-3]
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

            if inputValueIntoEquation(xi) < 0:
                signOfXi = negativeSign
            else:
                signOfXi = positiveSign

            error = calculateAbsoluteError(ai, bi)
            sublist = [i, ai, signOfAi, bi, signOfBi, xi, signOfXi, error]
            FalsePositionList.append(sublist)
            if error <= tolerance:
                break

        else:
            ai = previousIteration[1]
            bi = previousIteration[-3]
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

            error = calculateAbsoluteError(ai, bi)
            sublist = [i, ai, signOfAi, bi, signOfBi, xi, signOfXi, error]
            FalsePositionList.append(sublist)
            if error <= tolerance:
                break

def generateDiagram():
    pd.set_option('display.float_format', lambda x: f"{x:.{significantFigures}f}")
    pd.set_option('display.colheader_justify', 'center')
    df = pd.DataFrame(FalsePositionList, columns=['i', 'ai', 'f(ai)', 'bi', 'f(bi)', 'xi', 'f(xi)', 'Ei'])
    df.set_index('i', inplace=True)
    print(df)
    print('\n')

generateDiagram()
print("Answer: ", FalsePositionList[-1][-3], " +/- ", FalsePositionList[-1][-1], " *ROUND TO 3 DIGITS BOTH (ACCORDING TO VIDEO) "
                                                           "OR SOMETHING APPROPRIATE")