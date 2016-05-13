# ---------------------------------------------------------------------------
# Solves a differential equation numerically and then compares it to the perfect result
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint

def F(X, t):
    return np.array([X[2],X[3],0.0,-1.0])

# Do an integration using Eulers algorithm
def Euler(F, ini, t):
    list = []

    result = 1*ini
    list.append(1*ini)
    deltaT = t[1]-t[0]
    for i in t:
        result += deltaT * F(result, t)
        list.append(1*result)

    return list

# DO an integration using RungKutta algorithm
def RungaKutta2(F,ini,T):
    list = []

    result = 1*ini
    list.append(1*ini)
    deltaT = t[1]-t[0]
    for i in t:
        result += 1/2 * deltaT * (F(result, t) + F(result + deltaT*F(result, t), t))
        list.append(1*result)

    return list

ini = np.array([0.0,0.0,1.0,5.0])
t = np.linspace(0,10,11)
z = Euler(F,ini, t)
z2 = RungaKutta2(F, ini, t)

z=np.array(z)
z2=np.array(z2)

pl.scatter(z[:,0],z[:,1], color='g')
pl.scatter(z2[:,0],z2[:,1],color='r')
pl.plot(t, t*(5-t/2), color='b')
pl.axes().set_aspect('equal')
pl.show()

