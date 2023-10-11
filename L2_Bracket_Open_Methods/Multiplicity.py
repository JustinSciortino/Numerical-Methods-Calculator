from sympy import symbols, diff, cos, exp, sin, ln, log, factorial
import pandas as pd
x = symbols('x')

#GRAPH THE FUNCTION TO DETERMINE IF IT IS EVEN OR ODD
    #Odd - crosses the x axis
    #Even - touches the x axis
#input the values
equation = (x**4)+(17.2*x**3)+(69.16*x**2)-41.28*x+(5.76)
xr = -8.87056 #initial guess
significantFigures = 16 #significant figures
EvenGraph = True # both can't be true at the same time
OddGraph = False




multiplicityList = []
answer = [] #hold the answer, should be len = 1 at the end of the recursion

def findMultiplicity(): #input xr value
    foundFirstNonZero = False
    initialMultiplicity = len(multiplicityList)
    if initialMultiplicity == 0:  # f^i(xr)
        xrValue = equation.subs(x, xr)
        xrValue = xrValue.evalf(significantFigures)
        if abs(xrValue) < 1:
            sublist = [initialMultiplicity, "f(Xr)", xrValue]  # index, f^i(xr) and its value
            multiplicityList.append(sublist)
            findMultiplicity()
    else:
        nextMultiplicity = len(multiplicityList)
        der = diff(equation, x, nextMultiplicity)
        xrValue = der.subs(x, xr)
        xrValue = xrValue.evalf(significantFigures)
        if abs(xrValue) < 1:
            sublist = [nextMultiplicity, "f"+"'"*nextMultiplicity+"(Xr)", xrValue]  # index, f^i(xr) and its value
            multiplicityList.append(sublist)
            findMultiplicity()
        else:
            sublist = [nextMultiplicity, "f"+"'"*nextMultiplicity+"(Xr)", xrValue]  # index, f^i(xr) and its value
            multiplicityList.append(sublist)
            foundFirstNonZero = True

    if foundFirstNonZero:
        if EvenGraph:
            lastSublist = multiplicityList[-1]
            secondToLastSublist = multiplicityList[-2]
            if secondToLastSublist[0] % 2 == 0:
                mValue = secondToLastSublist[0]
                answer.append(mValue)
            else:
                mValue = lastSublist[0]
                answer.append(mValue)

        if OddGraph:
            lastSublist = multiplicityList[-1]
            secondToLastSublist = multiplicityList[-2]
            if secondToLastSublist[0] % 2 != 0:
                mValue = secondToLastSublist[0]
                answer.append(mValue)
            else:
                mValue = lastSublist[0]
                answer.append(mValue)

def generateAnswer():
    findMultiplicity()
    print("Multiplicity (m) = ", answer[0])

    df = pd.DataFrame(multiplicityList, columns=['i', 'f^m(xi)', 'Xi Value'])
    df.set_index('i', inplace=True)
    print(df)
    print('\n')

generateAnswer()