"""
Implementations for a Circle class

"""
from math import pi


class Circle1:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 2 * pi * self.radius
        self.area = pi * self.radius ** 2


class Circle2:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


class Circle3:
    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    @property
    def area(self):
        return pi * self.radius ** 2


print("""setting:
    c1 = Circle1(4)
    c2 = Circle2(4)
    c3 = Circle3(4)""")

c1 = Circle1(4)
c2 = Circle2(4)
c3 = Circle3(4)

print("-" * 60)
print("Circle1 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c1.radius, c1.perimeter, c1.area))
print("Circle2 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c2.radius, c2.perimeter(), c2.area()))
print("Circle3 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c3.radius, c3.perimeter, c3.area))

print("-" * 60)

print("looking at details")
print("setting c1.radius=100, c2.radius=100, c3.radius=100")
c1.radius = 100
c2.radius = 100
c3.radius = 100
print("Circle1 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c1.radius, c1.perimeter, c1.area))
print("Circle2 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c2.radius, c2.perimeter(), c2.area()))
print("Circle3 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c3.radius, c3.perimeter, c3.area))
print("Only Circle2 and Circle3 produce the correct behavior")

print("-" * 60)

print("Furthermore with Circle1 implementation we can set the attributes directly!")
print("c1.perimeter = 0 , c1.area = 0 ")
c1.perimeter = 0
c1.area = 0
print("Circle1 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c1.radius, c1.perimeter, c1.area))
print("!!!")

print("-" * 60)

print("With Circle2 implementation we can overwrite the attributes!")
print("c2.perimeter = 0 , c2.area = 0 ")
c2.perimeter = 0
c2.area = 0
try:
    print("Circle2 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c2.radius, c2.perimeter(), c2.area()))
except TypeError as e:
    print("Cannot print the results anymore", e)

print("-" * 60)

print("Correct way is Circle3")
print("trying to set c3.perimeter=0 , c3.area=0")
try:
    c3.perimeter = 0
    c3.area = 0
except AttributeError as e:
    print("Failed", e)
finally:
    print("Circle3 class, radius: % 5.2f, perimeter: %5.2f, area: %5.2f" % (c3.radius, c3.perimeter, c3.area))
print("-" * 60)

