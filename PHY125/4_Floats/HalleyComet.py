#! python
# ---------------------------------------------------------------------------
# Does some float precision testing
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import math
from matplotlib import pyplot as plt

e = 0.967
a = 17.8

E = []
MOldValues = []
M = 0

curE = 0
step = 0.1

# Find some values for E to plot the orbit
while (M not in MOldValues and M < 2*math.pi and M >= 0):
    MOldValues.append(M)
    E.append(curE)
    curE = curE + step
    M = curE - e * math.sin(curE)
    
# Create lists for the coordinates to plot the orbit
x = []
y = []

for EValue in E:
    x.append(a * (math.cos(EValue)-e))
    y.append(a * (math.sqrt(1-math.pow(e, 2))*math.sin(EValue)))

plt.plot(x, y, linestyle="", marker="o", color="b")
plt.plot([0], [0], marker="o", color="y")
plt.show()
