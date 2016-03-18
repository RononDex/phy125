# ---------------------------------------------------------------------------
# Solves assignement 2 up to a given precision
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

oldValues = []

# The function which needs to equal 0
def func(x):
    return x**3 + x - 84

# The derivative of the function
def funcPrime(x):
    return 3*x**2 +1

# Set some start value
start = 2.5
x = start

# execute approximation until we reach maximum point of accuracy
# (when formula yields already old calculated value)
# as a float (32-bit float, not double) is exactly precise to the 16th decimal point
# we can use this to our advantage to get to the result with less code
while (x not in oldValues):
    oldValues.append(x)    
    x = x - (func(x) / funcPrime(x))
    

print(x)
