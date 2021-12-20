import math
import numbers

class Circle:
    def __init__(self, radius):

        self.radius = radius

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius**2
 
    def __add__(self, other):
        if isinstance(other, Circle) is False:
            raise TypeError
        radius  = math.sqrt((self.area + other.area) / math.pi)
        return Circle(radius=radius)
    
    def __sub__(self, other):
        area_diff = self.area - other.area
        if isinstance(other, Circle) is False:
            raise TypeError
        if area_diff < 0:
            raise ValueError
        else: 
            radius  = math.sqrt((self.area - other.area) / math.pi)
            return Circle(radius=radius)
        
    def __mul__(self, other):
        if isinstance(other, numbers.Number) is False:
            raise TypeError
        elif other < 0:
            raise ValueError
        else: 
            radius = math.sqrt(self.area * other / math.pi)
            return Circle(radius=radius)
        
    def __truediv__(self, other):
        if isinstance(other, numbers.Number) is False:
            raise TypeError
        elif other < 0:
            raise ValueError
        else:
            radius = math.sqrt(self.area / (other * math.pi))
            
            return Circle(radius=radius)  
            
