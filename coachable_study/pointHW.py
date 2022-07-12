import sys
import math
import stddraw


class Point:
    
        def __init__(self, x0, y0):
            self._x0 = x0
            self._y0 = y0
        def toString(self):
            return (str(self._x0) + ", " + str(self._y0))
        def draw(self):
            stddraw.point(self._x0, self._y0)
        def drawTo(self, that):
            stddraw.line(self._x0, self._y0, that._x0, that._y0)
        def distanceTo(self, that):
            xdif = self._x0-that._x0
            ydif = self._y0-that._y0
            return math.sqrt((xdif * xdif) +(ydif *ydif))
            
