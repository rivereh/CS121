"""
    CS121 W18
    POLYGON CONSTRUCTOR
    RIVER HILL, JIN
    2/19/18
    PYTHON 3.6.4
"""
import math

# class for creating polygons
class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getPerimeter(self):
        return self.__n * self.__side
    def getArea(self):
        return (self.__n * pow(self.__side, 2)) / (4 * math.tan(math.pi / self.__n))
    def getSide(self):
        return self.__side
    def getN(self):
        return self.__n
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setSide(self, side):
        self.__side = side
    def setN(self, n):
        self.__n = n
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y


def main():
    # create three different polygons and store
    # them in an array
    poly1 = RegularPolygon()
    poly2 = RegularPolygon(6, 4)
    poly3 = RegularPolygon(10, 4, 5.6, 7.8)

    poly = [poly1, poly2, poly3]

    # loop through each element and print the
    # perimeter and area
    for x in range(len(poly)):
        print("Poly", (x + 1), "Perimeter:", poly[x].getPerimeter())
        print("Poly", (x + 1), "Area:", poly[x].getArea(), "\n")


main()
