import math
import numbers

class Vector:
    """
    class to work with vectors without help of numpy
    vector1 = Vector(list) = Vector(tuple)

    """
    def __init__(self, vector):

        self.source = vector
        if isinstance(vector, Vector) is True:
            self.source = vector.source
            
        self.x = self[0]
        self.y = self[1]
        self.z = self[2]
            
    @property
    def magnitude(self):
        mag = sum([x**2 for x in self])**0.5
        return mag
    
    @property
    def direction(self):
        return self / self.magnitude
    
    def distance(self, vector):
        """
        Returns the distance between two points
        """

        dist = sum([(x - y)**2 for x, y in zip(self, vector)])**2

        return dist

    def angle(self, vector):
        """
        return the angle between two vectors
        """
        vector = Vector(vector)
        cos = self.dot(vector) / (self.magnitude * vector.magnitude)

        return math.acos(cos)


    def dot(self, vector):
        """
        returns the dot product of two vectors
        """
        if isinstance(vector, Vector) is False:
            vector = Vector(vector)
        result = sum([x*y for x, y in zip(self, vector)])

        return result

    def cross(self, vector):
        """
        returns the cross product of two vectors
        """

        a1, a2, a3 = self
        b1, b2, b3 = vector
        result = [a2*b3 - a3*b2,
                  a1*b3 - a3*b1,
                  a1*b2 - a2*b1]

        return Vector(result)
    
    def plot(self):
        from mpl_toolkits import mplot3d
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        
        xline = [0, self[0]]
        yline = [0, self[1]]
        zline = [0, self[2]]
        ax.plot3D(xline, yline, zline, 'gray')
        plt.show()

    
    def __getitem__(self, item):
        """
        This does some magic
        """
        return self.source[item]

    def __repr__(self):
    
        return "Vector(%s)" % self.source    
    
    def __add__(self, other):
        """
        Define addition of vectors and forbid the addition with other objects
        """
        if not isinstance(other, (self.__class__, list, tuple)):
            raise TypeError(
                'Can only operate on {0}.'.format(self.__class__.__name__))
            
        else:
            return Vector([i + j for i, j in zip(self, other)])

    def __sub__(self, other):
        """
        Define subtraction of vectors and forbid it with other objects
        """
        if not isinstance(other, (self.__class__, list, tuple)):
            raise TypeError(
                'Can only operate on {0}.'.format(self.__class__.__name__))
            
        else:
            return Vector([i - j for i, j in zip(self, other)])

    def __mul__(self, other):
        """
        Define what can be multiplied and what not
        """
        if not isinstance(other, numbers.Number):
            raise TypeError
        else:
            return Vector([j*other for j in self])
        

    def __truediv__(self, other): # __truediv__???
        """
        Define what can be divided and what not
        """
        if not isinstance(other, numbers.Number):
            raise TypeError
        else:
            return Vector([j/other for j in self])
        
    def __lt__(self, other):
        if not isinstance(other, (self.__class__, list, tuple)):
            raise TypeError
        else:
            return self.magnitude < Vector(other).magnitude

        
    def __eq__(self, other):
        if not isinstance(other, (self.__class__, list, tuple)):
            raise TypeError
        else:
            v = Vector(other)
            return self[0] == v[0] and self[1] == v[1] and self[2] == v[2]
        

    def __repr__(self):
        s = "Vector([%s, %s, %s])" % (self[0], self[1], self[2])
        return s

