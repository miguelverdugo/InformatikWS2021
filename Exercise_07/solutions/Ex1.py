
from math import pi

class Circle1:
    def __init__(self, radius):

        self.radius = radius
        self.perimeter = 2*pi*self.radius
        self.area = pi*self.radius**2

class Circle2:
    def __init__(self, radius):

        self.radius = radius

    def perimeter(self):
        return 2*pi*self.radius

    def area(self):
        return pi*self.radius**2

class Circle3:
    def __init__(self, radius):

        self.radius = radius

    @property
    def perimeter(self):
        return 2*pi*self.radius

    @property
    def area(self):
        return pi*self.radius**2
