approx_I = 153.7 #equal to f(a) + f(b)
a = 3
b = 5

#input initial condition f(xo) = yo
xo = 4
yo = 24.2
m = 2

h = (b-a)/m

approx = (0.5)*(approx_I + 2*yo)
print("The new approximation I: ", approx)