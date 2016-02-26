# ---------------------------------------------------------------------------
# Calculates the bernoulli number for the given n.
# Also contains some performance optimisiations
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

from sympy import Rational as Frac
import time

# global variable to cache already calculated values
cacheBernoulli = []

# Since the Python interpreter calls the C++ wrapper for every cache.insert() call,
# we can call cachec.insert once and store the function inside a variable
# This causes the python interpreter to call the C++ wrapper only once, resulting
# in a smaller overhead.
insertBernoulli = cacheBernoulli.insert

# Calculates the bernoulli value for the giving iteration (recursive)
def Bernoulli(n):
    global cacheBernoulli
    global insertBernoulli

    if n == 0:
        return Frac(1, 1)

    # Try to access the item in the cache
    try:
        return cacheBernoulli[n]
    except:    
        curValue = 0

    # As the Factorial value of n is the same throughout the whole for loop,
    # we can calculate its value and then store it in a variable so we have a cached value
    fracN = Factorial(n)

    for k in range(0, n):

        # If k is uneven, the value is 0,
        # no calculation needed in this case
        valueK = int(0)
        if k % 2 == 0 or k == 1:
            valueK = Bernoulli(k)

        top = Frac(1,1) * fracN / ( Factorial(k) * Factorial(n - k + 1) )
        curValue += top * valueK

    insertBernoulli(n, -curValue)
    return -curValue

# Calculates the Factorial for the given number
def Factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

#--------------------------------------
# Main execution (procedural)
#--------------------------------------

# ask the user to input the bernoulli iteration he/she wants to calculate
n = int(input("Which iteration of bernoutlli numbers do you want to calculate? "))


print("Calculating Bernoulli(%s)..." % n)

# store the time when the executation starts, 
# so we can measure how long it took to calculate
startTime = time.time()

# Calculate the given iteration of bernoulli numbers and output to console
print("Result: %s" % Bernoulli(n))

# Calculate time it took to calcualte the number and output to console
print("Took %s seconds" % (time.time() - startTime))