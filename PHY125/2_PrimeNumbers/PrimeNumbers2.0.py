# ---------------------------------------------------------------------------
# Calculates prime numbers in a defined range using the method of Eratosthenes (Zusatzaufgabe)
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------
from pylab import *
import time

def FindPrimeNumbers(n):

    primesTemp = [True]*(n+1)
    primesTemp[0] = primesTemp[1] = False
    primes = []

    for i in range(2, n+1):
        if (primesTemp[i]):
            primes.append(i)
            for j in range(2*i, n+1, i):
                primesTemp[j] = False

    return primes

end = 1000000
print("Searching for Primes in 0-%s" % end)

start = time.time()

primes = FindPrimeNumbers(end)

print("Took %s seconds" % (time.time() - start))

print(primes[840])
