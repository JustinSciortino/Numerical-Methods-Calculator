from sympy import symbols, diff, cos, exp, sin, ln, log, factorial
import pandas as pd

def FixedPoint(equation, m, significantFigures, xo, tolerance):
    x = symbols('x')


    #input the values, equation must be in the form of g(x) = x
    #if the Ei is increasing quickly as i increases, function is diverging and pick a new g(x)
    #equation = (x**3)*sin((3*x)+4)-4
    #m = 1 #multiplcity of the root
    #significantFigures = 16 #significant figures
    #xo = 7 #initial guess
    #tolerance = 1e-12   #tolerance value


    forwardDerivative = diff(equation, x, m)
    derivative = diff(equation)
    secondDerivative = diff(derivative)
    absolute = [] #empty list containing sub lists of the i, Xi , Xi+1, Ei
    relative = [] #empty list containing sub lists of the i, Xi , Xi+1, ei
    forward = [] #empty list containing sub lists of the i, Xi , Xi+1, forward


    def calculateNewtonScheme(xi): #calculate Xi+1
        equation_xo = equation.subs(x, xi)
        derivative_xo = derivative.subs(x, xi)
        newtonScheme = xi - (equation_xo / derivative_xo)
        numerical_result = newtonScheme.evalf(significantFigures)
        return numerical_result

    def calculateAbsoluteError(xi):  
        i = len(absolute) #iterator
        nextXi = calculateNewtonScheme(xi)

        if i == 0:
            sublist = [i, xi, nextXi, "N/A"]
            absolute.append(sublist)
            calculateAbsoluteError(nextXi)

        else:
            index = len(absolute)
            previousXi = absolute[index-1][1]
            result = abs(xi - previousXi)
            if result <= tolerance:
                sublist = [index, xi, nextXi, result]
                absolute.append(sublist)
                print("X",index," value is ", xi)
            else:
                sublist = [i, xi, nextXi, result]
                absolute.append(sublist)
                calculateAbsoluteError(nextXi)

    def AbsoluteError():
        print("ABSOLUTE ERROR")
        calculateAbsoluteError(xo)
        df = pd.DataFrame(absolute, columns=['i', 'Xi', 'Xi+1', 'Ei'])
        df.set_index('i', inplace=True)
        print(df)
        print('\n')

    def calculateRelativeError(xi):
        i = len(relative)  # iterator
        nextXi = calculateNewtonScheme(xi)

        if i == 0:
            sublist = [i, xi, nextXi, "N/A"]
            relative.append(sublist)
            calculateRelativeError(nextXi)

        else:
            index = len(relative)
            previousXi = relative[index - 1][1]
            result = abs((xi - previousXi)/xi)
            if result <= tolerance:
                sublist = [index, xi, nextXi, result]
                relative.append(sublist)
                print("X",index," value is ", xi)
            else:
                sublist = [i, xi, nextXi, result]
                relative.append(sublist)
                calculateRelativeError(nextXi)

    def RelativeError():
        print("RELATIVE ERROR")
        calculateRelativeError(xo)
        df = pd.DataFrame(relative, columns=['i', 'Xi', 'Xi+1', 'ei'])
        df.set_index('i', inplace=True)
        print(df)
        print('\n')

    def calculateForwardError(xi):
        i = len(forward)  # iterator
        nextXi = calculateNewtonScheme(xi)

        if i == 0:
            sublist = [i, xi, nextXi, "N/A"]
            forward.append(sublist)
            calculateForwardError(nextXi)

        else:
            index = len(forward)
            result = (abs((factorial(m)*equation.subs(x, xi))/(forwardDerivative.subs(x, xi))))**1/m
            if result <= tolerance:
                sublist = [index, xi, nextXi, result]
                forward.append(sublist)
                print("X",index," value is ", xi)
            else:
                sublist = [i, xi, nextXi, result]
                forward.append(sublist)
                calculateForwardError(nextXi)

    def ForwardError():
        print("FORWARD ERROR")
        calculateForwardError(xo)
        df = pd.DataFrame(forward, columns=['i', 'Xi', 'Xi+1', 'Forward'])
        df.set_index('i', inplace=True)
        print(df)
        print('\n')

    def calculateLambda(r):
        formula = abs(secondDerivative.subs(x, r)/(2*derivative.subs(x,r)))
        formula = formula.evalf(significantFigures)
        return formula

    def calculateErrorMagnificationFactor(xr):
        formula = 1/(abs(secondDerivative.subs(x, xr)))
        formula = formula.evalf(significantFigures)
        return formula

    AbsoluteError()
    RelativeError()
    ForwardError()
    l = calculateLambda(xo)
    M = calculateErrorMagnificationFactor(xo)
    print("The Asymptotic Error constant/Lambda is: ",l)
    print("The Error Magnification Factor (M) is: ",M)