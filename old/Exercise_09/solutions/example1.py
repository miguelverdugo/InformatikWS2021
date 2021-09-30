

class Circle1:
    """
    This is a correct implementation and nothing else is actually needed
    The main problem is that after creating an instance is still possible
    to change the attributes directly at runtime and the rest are not updated
    """
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 2 * 3.14156 * self.radius
        self.area = 3.14156 * self.radius**2


class Circle2:
    """
    This is also correct. A problem is that to call the calculations
    additional parentesis are needed when no parameters are entered.
    Another problem is that is still possible to set up the methods as attributes
    in runtime creating eventually further problems.
    """
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14156 * self.radius

    def area(self):
        return 3.14156 * self.radius**2


class Circle3:
    """
    This is probably an optimal implementation as the attributes cannot be set
    in runtime. It also doesn't need parentheses. If self.radius is updated
    the rest of the properties are updated too.
    """
    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * 3.14156 * self.radius

    @property
    def area(self):
        return 3.14156 * self.radius**2

        
