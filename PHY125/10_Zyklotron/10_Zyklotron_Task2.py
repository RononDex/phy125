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
    omega = 2
    return np.array([X[2],X[3],2*X[3],-2*X[2]+math.cos(omega*t)])

# Do an integration using Eulers algorithm
def Euler(F, ini, t):
    list = []

    result = 1*ini
    list.append(1*ini)
    deltaT = t[1]-t[0]
    for i in t:
        result += deltaT * F(result, i)
        list.append(1*result)

    return list

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

ini = np.array([0.0,0.0,0,0])
t = np.linspace(0,10,1000)
z = Euler(F,ini, t)
z2 = RungaKutta2(F, ini, t)

z=np.array(z)
z2=np.array(z2)

pl.scatter(z[:,0],z[:,1], color='g')
pl.scatter(z2[:,0],z2[:,1],color='r')
pl.axes().set_aspect('equal')
pl.show()

