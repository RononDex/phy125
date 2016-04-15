# ---------------------------------------------------------------------------
# Solves the problem with a 3-dimensional resistor grid
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

from pylab import figure, show, imread, imshow, contourf
from pylab import array, linspace, pi, sin
from numpy import matrix as matrixNumpy
from matplotlib.animation import FuncAnimation
from itertools import count
from time import time, gmtime
import math

class Map(object):
    """ class showing a map with some contour on it

    Attributes
    ----------
    levels : levels used for the colormap

    """
    
    #-------------------------------------------------------------------------------
    # Some comments on the map class from my part of view:
    #-------------------------------------------------------------------------------
    # For better readability and easier understanding I declared all the global variables in the header of the class
    # The constructor is only to initiazlize variables that depend on parameters passed to the constructor
    # Furhermore variables starting with "_" are only for hidden private fields behind properties (according to Camel case)
    # Naming global variables with the prefix "_" was very confusing for me (coming from C-languages), which is why I renamed all the 
    # functions and variables to Camel case
    # -------------------------------------------------------------------------------

    height = 0
    width = 0
    levels = linspace(-1, 1, 13)
    img = None
    fig = figure()
    axes = None

    def __init__(self, map_source="karte.png"):
        """ initialise a Map instance

        Parameters
        ----------
        map_source : string
            map-image to use for the background

        """
        self.img = imread(map_source)
        self.axes = self.fig.add_subplot(111)
        self.axes = self.fig.add_subplot(111)
        self.axes.xaxis.set_visible(False)
        self.axes.yaxis.set_visible(False)
        self.height = self.img.shape[0]
        self.width = self.img.shape[1]

    def ShowTime(self, t):
        """ show map and contour for a given time t

        Parameters
        ----------
        t : gmtime
            gmtime object for the rendering time

        """    

        inclination = math.radians(23.5)
        imshow(self.img)
        N = 10
        x = linspace(0, self.width, 2*N)
        y = linspace(0, self.height, N)
        z = self.CalculateGrid(t, N)
        contourf(x, y, z, self.levels, cmap="hot", alpha=0.5)

    # Calculates the zenit vector
    def CalcZenitVector(self, lat, long, inc, dayAngle, yearAngle):
        Rx = Map.GetRotationmatrixX(inc)
        Ry = Map.GetRotationmatrixY(-lat)
        Rz = Map.GetRotationmatrixZ(long + dayAngle + yearAngle)
        
        ex = matrixNumpy(
                        [1, 0, 0]
                    )        

        zenit = ex * Ry * Rz * Rx
        return zenit

    # Calculates the earth-sun vector 
    def CalcSunVector(self, angleYear):
        Rz = Map.GetRotationmatrixZ(angleYear)
        ex = matrixNumpy(
                        [1, 0, 0]
                    )
        return ex * Rz

    # Creates the grid for the z axis of the contour
    def CalculateGrid(self, t, N):
        # Create an empty grid of dimensions N x 2N
        grid = [[0 for x in range(2*N)] for x in range(N)]
        inclination = math.radians(23.5)

        dayAngle = ((t.tm_hour+(t.tm_min/60))/24)*2*pi
        yearAngle = ((t.tm_yday -79) / 365)*2*pi
        
        # Populate the grid with the correct values
        for x in range(2*N):
            for y in range(N):
                lat = (((pi / N) * y)) - pi/2
                long = (2*pi / (2*N) * x)
                zenit = self.CalcZenitVector(lat, long, inclination, dayAngle, yearAngle)
                sun = self.CalcSunVector(yearAngle)
                res = sun * zenit.T
                grid[y][x] = float(res)* (-1)
        return grid
                

    def ShowAnimation(self, speed=1800, fps=10):
        """ show animated contour on map

        Parameters
        ----------
        speed : int or float
            seconds passing in the animation for each realtime second
        fps : int
            frames per second of the animation

        """

        def Frame(n):
            """ draw frame n of the animation

            Parameters
            ----------
            n : int
                number of frame to draw (use to calculate time)

            """
            # reset frame before drawing
            self.axes.clear()
            # calculate new time (seconds since Epoche)
            t = gmtime(n*speed)
            # call drawing function
            self.ShowTime(t)

        anim = FuncAnimation(self.fig, Frame, count(), interval=1000/fps)
        show()

    def ShowNow(self):
        """ show the contour for now on the map """
        self.ShowTime(gmtime())
        show()

    def Run(self):
        """ helper to control the show-function from the commandline

        if the string 'animate' is given on the commandline, run the animation
        otherwise show countours corresponding to now.

        """
        import sys
        if "animate" in sys.argv:
            self.ShowAnimation()
        else:
            self.ShowNow()

    # Create the RotationMatrix for X-axis
    @staticmethod
    def GetRotationmatrixX(angle):
        return matrixNumpy([
            [1, 0, 0],
            [0, math.cos(angle), math.sin(angle)],
            [0, -math.sin(angle), math.cos(angle)]
        ])

    # Create the RotationMatrix for Y-axis
    @staticmethod
    def GetRotationmatrixY(angle):
        return matrixNumpy([
            [math.cos(angle), 0, -math.sin(angle)],
            [0, 1, 0],
            [math.sin(angle), 0, math.cos(angle)]
        ])

    # Create the RotationMatrix for Z-axis
    @staticmethod
    def GetRotationmatrixZ(angle):
        return (matrixNumpy([
            [math.cos(angle), math.sin(angle), 0],
            [ -math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]
        ]))


if __name__ == "__main__":
    demo = Map()
    demo.ShowAnimation()