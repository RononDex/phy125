# ---------------------------------------------------------------------------
# Solves a differential equation numerically
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint
import math

def F(X, t):
    omega = 0.5
    return np.array([X[2],X[3],0,-math.sin(X[1])-2*math.sin(X[1]-omega*X[0])])

# DO an integration using RungKutta algorithm
def RungaKutta2(F,ini,T):
    list = []

    result = 1*ini
    list.append(1*ini)
    deltaT = t[1]-t[0]
    for i in t:
        result += 1/2 * deltaT * (F(result, i) + F(result + deltaT*F(result, i), i))
        list.append(1*result)

    return list

ini = np.array([0.0,0.0,1,0])
t = np.linspace(0,50,1000)
z2 = RungaKutta2(F, ini, t)

z2=np.array(z2)

pl.scatter(z2[:,0],z2[:,1],color='r')
pl.axes().set_aspect('equal')
pl.show()

