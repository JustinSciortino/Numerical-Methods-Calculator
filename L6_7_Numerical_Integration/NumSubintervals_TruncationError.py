from math import ceil
absoluteTruncationError = 0.01
numberOfSubintervals = 10
abTruncLessThan = 0.00001
order = 3

m = numberOfSubintervals*((absoluteTruncationError/abTruncLessThan)**(1/order))
mRounded = ceil(m)
print("Any value above ", mRounded, "is an answer.")