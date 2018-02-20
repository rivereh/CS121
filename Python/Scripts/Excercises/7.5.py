"""
    CS121 W18
    POLYGON CONSTRUCTOR
    RIVER HILL
    2/19/18
    PYTHON 3.6.4
"""
import math

class RegularPolygon():
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.n = n
        self.side = side
        self.__x = x
        self.__y = y
    def getPerimeter(self):
        return self.n * self.side
    def getArea(self):
        return (self.n * pow(self.side, 2)) / (4 * math.tan(math.pi / self.n))
    def getSide(self):
        return self.side
    def getN(self):
        return self.n
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setSide(self, side):
        self.side = side
    def setN(self, n):
        self.n = n
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

