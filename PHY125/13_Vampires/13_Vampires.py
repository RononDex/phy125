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
    fxCopy = fx*1

    # Vampire movement phase
    for i in range(1, len(fx)-1):
        # Half of the vampires move from the left "pixel" to this one
        fx[i] += fxCopy[i-1]*0.5
        fx[i-1] -= fxCopy[i-1]*0.5

        # Half of the vampires move from the right "pixel" to the current one
        fx[i] += fxCopy[i+1]*0.5
        fx[i+1] -= fxCopy[i+1]*0.5

    # Vampire bite phase
    for i in range(0, len(fx)):
        # From the video we know that the number of bites is proportional to n_vampires * n_persons
        fx[i] += fx[i] * (1-fx[i])

    return fx

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