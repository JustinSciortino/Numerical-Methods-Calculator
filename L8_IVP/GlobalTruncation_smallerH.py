"""
You are approximating the solution of an initial value problem using a RK2 method.
If the global truncation error of the approximation produced by the VP solver in t = 5 is 0.6
when using a step size h = 0.01, how much will be the global truncation error when using
a smaller step size of h = 0.001?
"""

error = 0.1
h1 = 0.01
h2 = 0.001
order = 6 #if RK2 = 2, if RK4 = 4, if RK5 = 5, etc.

answer = error * ((h2 / h1) ** order)
formatted_answer = format(answer, '.10f')

print("For the final exam, answer could be in scientific notation or not.")
print("Answer:", formatted_answer)
print("Answer:", answer)