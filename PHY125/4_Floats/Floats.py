#! python
# ---------------------------------------------------------------------------
# Does some float precision testing
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import math

""" Versuche: 0.01, 0.001, ... """
start = 0.1
epsilon = 0.1
nullstellen = 1
while (1 != 1+epsilon):
    epsilon = start / (math.pow(10, nullstellen))
    nullstellen = nullstellen + 1
print("1 == 1+epsilon:  ", 1 == 1+epsilon, " Nullstellen: ", nullstellen-1)

""" Versuche: 1e-301, 1e-302, ... """
epsilon = 1e-300
start = 1
exponent = -300
while (not math.pow(10, exponent) == 0):
    epsilon = start * (math.pow(10, exponent))
    exponent = exponent - 1
epsilon = epsilon / 10
    
print("epsilon/2 == 0.0:", epsilon/2 == 0.0, " Exponent: ", exponent)

""" Versuche: 2.0**46, 2.0**47, ... """
N = 2.0**45
start = 2.0
exponent = 45
while (not N+1.0 == N):
    N = math.pow(start, exponent)
    exponent = exponent + 1
print ("N+1 == N:        ", N+1.0 == N, " Exponent: ", exponent-1)