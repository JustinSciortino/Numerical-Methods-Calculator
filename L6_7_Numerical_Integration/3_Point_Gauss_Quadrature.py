from sympy import symbols, ln, cos, exp, sin, sqrt, pi

x = symbols('x')
t = symbols('t')

a = 1
b = 3
significant_digits = 8
equation = (x**2)*ln(x)

Interpolating_2_Points = False
Interpolating_3_Points = True
Interpolating_4_Points = False
Interpolating_5_Points = False

def Three_Interpolating_Points():
    c1 = 0.5555555555555556
    c2 = 0.8888888888888888
    c3 = 0.5555555555555556
    cList = [c1, c2, c3]

    x1 = -0.7745966692414834
    x2 = 0
    x3 = 0.7745966692414834
    xiList = [x1, x2, x3]

    m = ((b-a)/2)
    r = ((b+a)/2)
    new_equation = m*t+r

    sum = 0
    for i in range(0,3):
        sum += cList[i] * equation.subs(x, new_equation.subs(t, xiList[i]))

    answer = m * sum
    print("The value of the integral is with 3 interpolating points: ", answer.evalf(significant_digits))

def Two_Interpolating_Points():
    c1 = 1
    c2 = 1
    cList = [c1, c2]

    x1 = -0.5773502691896257
    x2 = 0.5773502691896257
    xiList = [x1, x2]

    m = ((b - a) / 2)
    r = ((b + a) / 2)
    new_equation = m * t + r

    sum = 0
    for i in range(0, 2):
        sum += cList[i] * equation.subs(x, new_equation.subs(t, xiList[i]))

    answer = m * sum
    print("The value of the integral is with 2 interpolating points: ", answer.evalf(significant_digits))

def Four_Interpolating_Points():
    c1 = 0.3478548451374538
    c2 = 0.6521451548625461
    c3 = 0.6521451548625461
    c4 = 0.3478548451374538
    cList = [c1, c2, c3, c4]

    x1 = -0.8611363115940526
    x2 = -0.3399810435848563
    x3 = 0.3399810435848563
    x4 = 0.8611363115940526
    xiList = [x1, x2, x, x4]

    m = ((b - a) / 2)
    r = ((b + a) / 2)
    new_equation = m * t + r

    sum = 0
    for i in range(0, 4):
        sum += cList[i] * equation.subs(x, new_equation.subs(t, xiList[i]))

    answer = m * sum
    print("The value of the integral is with 4 interpolating points: ", answer.evalf(significant_digits))

def Five_Interpolating_Points():
    c1 = 0.2369268850561891
    c2 = 0.4786286704993665
    c3 = 0.5688888888888889
    c4 = 0.4786286704993665
    c5 = 0.2369268850561891
    cList = [c1, c2, c3, c4, c5]

    x1 = -0.9061798459386640
    x2 = -0.5384693101056831
    x3 = 0
    x4 = 0.5384693101056831
    x5 = 0.9061798459386640
    xiList = [x1, x2, x3, x4, x5]

    m = ((b - a) / 2)
    r = ((b + a) / 2)
    new_equation = m * t + r

    sum = 0
    for i in range(0, 5):
        sum += cList[i] * equation.subs(x, new_equation.subs(t, xiList[i]))

    answer = m * sum
    print("The value of the integral is with 5 interpolating points: ", answer.evalf(significant_digits))

if Interpolating_2_Points:
    Two_Interpolating_Points()
if Interpolating_3_Points:
    Three_Interpolating_Points()
if Interpolating_4_Points:
    Four_Interpolating_Points()
if Interpolating_5_Points:
    Five_Interpolating_Points()

