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

steps = 51
g = np.linspace(-1, 1, 51)
X,Y = np.meshgrid(g,g)

Z = X + 1j*Y
F = np.sin(Z).real

lastValue = F*1
while (not EvaluteConvergence(lastValue, F)):
    lastValue = F*1
    L = 0*F
    L[1:-1, 1:-1] = (F[1:-1,:-2] + F[1:-1,2:] + F[:-2,1:-1] + F[2:,1:-1]) /4
    F=0*L
    F[1:-1, 1:-1]=L[1:-1, 1:-1] 

levels = np.linspace(np.amin(F), np.amax(F),100)
pl.clabel(pl.contour(X,Y,F, levels=levels))
pl.axes().set_aspect('equal')
pl.show()