# ---------------------------------------------------------------------------
# Simulates the spreading of an idea of vampires
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

from __future__ import division
from numpy import linspace
from matplotlib.pyplot import figure, plot, show, axes, axis
from matplotlib.animation import FuncAnimation

def NextStep(fx):
    d2x = -2 * y
    d2x[1:-1] += y[2:] + y[:-2]
    d2x[0] += y[1]
    d2x[-1] += y[-2]
    d2x = d2x/dx/dx
    # then add the reaction terms
    dy = r * y * (1. - y/K) + D * d2x

def frame(_):
    global fx
    axes().clear()
    axis([-20, 20, -0.5, 1.5])
    fx = NextStep(fx)
    plot(x, fx)


x = linspace(-20,20, 200)

fx = 0*x
fx[99:101] = 1

plot(x, fx)

fig = figure()
anim = FuncAnimation(fig, frame, range(1000))
show()