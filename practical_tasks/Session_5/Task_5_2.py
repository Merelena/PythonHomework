from Task_5_1 import GeometricFigure
import math


class Circle(GeometricFigure):
    def area(self, r):
        return math.pi * r ** 2

    def parameter(self, r):
        return 2 * math.pi * r