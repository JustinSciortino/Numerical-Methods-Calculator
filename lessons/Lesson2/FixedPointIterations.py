from sympy import symbols, diff, cos, exp, sin, ln, log, factorial
import pandas as pd

def FixedPointIterations(equation, tolerance, r, xo):

    x = symbols('x')


    #Input the values below
    equation = (x+5)/(x+1)
    tolerance = 1e-3
    r = 2.24
    xo = 2.38


    derivative_of_equation = diff(equation, x)
    lambdaValue = abs(derivative_of_equation.subs(x, r))
    eo = abs(r-xo)
    listForValues = []

    i = 1
    while True:
        eValue = (lambdaValue**i)*eo
        listForValues.append([i, eValue])
        if eValue <= tolerance:
            print("Iteration: ", i)
            break
        else:
            i+=1

    pd.set_option('display.float_format', lambda x: f"{x:.{tolerance}f}")
    df = pd.DataFrame(listForValues, columns=['i', 'ei'])
    df.set_index('i', inplace=True)
    print(df)
    print('\n')