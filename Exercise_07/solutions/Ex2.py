
from math import pi

class Circle:
    def __init__(self, radius):

        self.radius = radius

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False


if __name__ == "__main__":

    c1 = Circle(radius=1)
    c2 = Circle(radius=1.0)
    c3 = Circle(radius=2)
    # the following statements should be always true
    print( (c1 < c3) is  True)
    print( (c2 > c1) is False)
    print( (c3 > c1) is True)
    print( (c1 == c2) is True)
    print( (c1 == c3) is  False)
