import pandas as pd
from math import sqrt



#Enter the values in lines 15 and 16
xi = [1,2,5,7]
yi =[2.1, 2.9, 6.1, 8.3]



def calculateSums(A):
    total = 0
    for k in A:
        total+=k
    return total
def findM():
    if len(xi) == len(yi):
        return len(xi)

xiyi = []
xiSquared = []
riSquared = []

m = findM()
i = 0
index = 0

while index !=len(xi):
    xVal = xi[index]
    yVal = yi[index]
    product = xVal*yVal
    xiyi.append(product)
    index+=1

for j in xi:
    squaredValue = j**2
    xiSquared.append(squaredValue)

sumXi = calculateSums(xi)
sumYi = calculateSums(yi)
sumXiYi = calculateSums(xiyi)
sumXiSquared = calculateSums(xiSquared)
aOne = ((m*sumXiYi)-(sumXi*sumYi))/((m*sumXiSquared)-(sumXi**2))
ao = (sumYi/m)-((aOne/m)*sumXi)

while i !=len(xi):
    xVal = xi[i]
    yVal = yi[i]
    rVal = (yVal-ao-aOne*xVal)**2
    riSquared.append(rVal)
    i+=1

SE = calculateSums(riSquared)

data = {
    'xi': xi + [sumXi],
    'yi': yi + [sumYi],
    'xiyi': xiyi + [sumXiYi],
    'riSquared': riSquared + [SE]
}
df = pd.DataFrame(data)
pd.set_option('display.precision', 16)

print(df.to_string(index=False, justify='left', col_space=20))
print("\nSE: ", SE)
print("MSE: ", SE/m)
print("RMSE: ", sqrt(SE/m))
print("a0: ", ao)
print("a1: ", aOne)
print("\nEquation: y = ", aOne, "x", " + ", ao)