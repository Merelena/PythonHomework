from Task_5_1 import GeometricFigure
import math


class Rectangle(GeometricFigure):
    def area(self, length, width):
        return length * width

    def parameter(self, length, width):
        return 2 * (length + width)

    def length_of_diagonals(self, length, width):
        return math.sqrt(length ** 2 + width ** 2)

    def fit_in_a_circle(self, length, width, r):
        if self.length_of_diagonals(length, width) == 2 * r:
            return True
        else: return False