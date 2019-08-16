from abc import ABC, abstractmethod


class GeometricFigure:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass