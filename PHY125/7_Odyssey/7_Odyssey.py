# ---------------------------------------------------------------------------
# Creates a pascal triangle and a random distribution
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import random
from scipy.stats import norm
from numpy import sqrt
import matplotlib.pyplot as plt
from matplotlib.mlab import frange

# Global variable to store the pascal triangle
pascalTriangle = None
pascalTriangleReference = None

# Creates a pascal triangle of the given depth
# and assigns it to the global variable "pascalTriangle"
def CreatePascalTriangle(depth):
    global pascalTriangle
    global pascalTriangleReference

    pascalTriangle = [None] * depth  
    pascalTriangleReference = [None] * depth  

    for x in range(1, depth+1):
        pascalTriangle[x-1] = [0]*x
        pascalTriangleReference[x-1] = [0]*x

        for y in range(0, x):
            if (y == 0 or y == x-1):
                pascalTriangleReference[x-1][y] = 1
            else:
                pascalTriangleReference[x-1][y] = pascalTriangleReference[x-2][y-1] + pascalTriangleReference[x-2][y]

# Creates the random distribution inside the pascal triangle
# for the given amount of iterations
def CreateRandomDistribution(iterations):
    global pascalTriangle

    pascalTriangle[0][0] = iterations
    
    # Create distrubition
    for x in range(0, iterations):
        position = 0
        for level in range(1, len(pascalTriangle)):
            possibleChoices = [ position, position+1]
            choice = random.choice(possibleChoices)
            pascalTriangle[level][choice] += 1
            position = choice
    
    # Normalise the values
    for x in range(0, len(pascalTriangle)):
        sum = 0
        for y in range(0, len(pascalTriangleReference[x])):
            sum += pascalTriangleReference[x][y]
        for y in range(0, len(pascalTriangle[x])):
            pascalTriangle[x][y] = round( pascalTriangle[x][y] / iterations * sum) *2
        for y in range(0, len(pascalTriangleReference[x])):
            pascalTriangleReference[x][y] += pascalTriangleReference[x][y]


def CreateGaussDistribution(level, x=None):
    """ Calculates the gaussian values corresponding to Pascal's trinagle

    Parameters
    ----------
    level : int
       level of pascals triangle to calculate values for
    x : array of floats or ints
       positions where the gaussian distribution should be evaluated
       default: positios in Pascal's Trinagle, numbered as 0, 1, ...


    Returns
    -------
    values : array of floats
        values corresponding to the given Positions


    Examples
    --------
    >>> pascal_gauss(1) # compare to [1, 1] from Pascal's Trinagle
    array([ 0.9678829,  0.9678829])

    >>> pascal_gauss(1, frange(-0.5, 1.5, 0.5)) # useful for plotting
    array([ 0.21596387,  0.9678829 ,  1.59576912,  0.9678829 ,  0.21596387])

    """
    if x is None:
        x = range(level+1)
    # norm.pdf(positions, mean, standard_deviation)
    return 2**level*norm.pdf(x, level/2,  sqrt(level/4))

depth = 20
CreatePascalTriangle(depth)

CreateRandomDistribution(10000)
gaussDistribution = CreateGaussDistribution(depth)

print(pascalTriangle)

plt.plot(pascalTriangle[-1])
plt.plot(gaussDistribution, color='g')
plt.plot(pascalTriangleReference[-1], color='r')
plt.show()