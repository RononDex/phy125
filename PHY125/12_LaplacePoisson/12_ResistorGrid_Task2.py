# ---------------------------------------------------------------------------
# Solves a partial differential equation numerically
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as pl
import math

def EvaluteConvergence(lastValue, curValue):
    for i in range(0, len(lastValue)):
        for j in range(0, len(lastValue[i])):
            delta = math.fabs(lastValue[i][j] - curValue[i][j])
            if delta > 0:
                return True
    return False

def CalcGrid(F, K):
    Q = 1*F[1:-1, 1:-1]
    for i in range(1, len(F)-2):
        for j in range(1, len(F[i])-2):
            w = 0
            if i == K+2 and j == K + 1:
                w = 1
            elif i == j == K:
                w = -1
            Q[i][j] = (F[i+1][j] + F[i-1][j]+F[i][j+1]+F[i][j-1]-w)/4
    F[1:-1, 1:-1] = Q
    return F
    

steps = 51
K=40
g = np.linspace(-1, 1, 51)
X,Y = np.meshgrid(g,g)
F = 0*(X+Y)

F = CalcGrid(F, K)

lastValue = F*1
while (not EvaluteConvergence(lastValue, F)):
    lastValue = F*1
    L = 0*F
    L[1:-1, 1:-1] = (F[1:-1,:-2] + F[1:-1,2:] + F[:-2,1:-1] + F[2:,1:-1]) /4
    F=0*L
    F[1:-1, 1:-1]=L[1:-1, 1:-1] 

levels = np.linspace(np.amin(F), np.amax(F),11)
pl.clabel(pl.contour(X,Y,F, levels=levels))
pl.axes().set_aspect('equal')
pl.show()