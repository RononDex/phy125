#! python
# ---------------------------------------------------------------------------
# Calculates pi until we reach the Feynman point
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

from sympy import Rational
import time

# Calculates the arctan for the defined value using the taylor expansion
# You can define the precision of the approximiation (iterations) through the 2nd parameter
def arctan(x, wantedPrecision):
    precisionReached = False
    res = Rational(0, 1)
    iteration = 1

    while (not precisionReached):
        res += (-1)**(iteration -1)*x**(2*iteration-1)/(2*iteration-1)
        iteration += 1
        if iteration == wantedPrecision:
            precisionReached = True

    return res

precision = 549
print("Calculating Pi...")
print("Precision (iterations) fror arctan approximiation is set to: %s" % precision)

# store the time when the executation starts, 
# so we can measure how long it took to calculate
startTime = time.time()

pi = 4*(4*arctan(Rational(1, 5), precision) - arctan(Rational(1, 239),precision))
print("PI: %s" % pi.evalf(769))

print("Took %s seconds" % (time.time() - startTime))