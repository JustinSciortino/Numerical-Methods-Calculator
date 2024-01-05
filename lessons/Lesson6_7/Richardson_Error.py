from sympy import *
x = symbols('x')

#Question of the form: You applied a composite quadrature formula of order 𝑂(h^5) to estimate a defined integral.
# When using 4 sub-intervals your estimation is 8.633 and when using 8 sub-intervals it is 8.634.
# The estimated absolute error for the value obtained with 8 sub-intervals is about

q = 6
h1 = 8
h2 = 4
I_h1 = 5.977
I_h2 = 5.976

def Richardon_Error(q, h1, h2, I_h1, I_h2):
    Error = abs((I_h2 - I_h1)/((h1/h2)**q-1))
    return Error
Richardon_Error(q, h1, h2, I_h1, I_h2)
print("The estimated absolute error for the value obtained with 8 sub-intervals is about: ", Richardon_Error(q, h1, h2, I_h1, I_h2))