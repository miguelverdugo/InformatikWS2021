import math


class Vector:
    """
    class to work with vectors without help of numpy
    vector1 = Vector(list) = Vector(tuple)

    """
    def __init__(self, vector):

        self.source = vector
        if isinstance(vector, Vector) is True:
            self.source = vector.source

    @property
    def magnitude(self):
        mag = sum([x**2 for x in self])**0.5
        return mag

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

    def __getitem__(self, item):
        """
        This does some magic
        """
        return self.source[item]

    def __repr__(self):
        return "Vector(%s)" % self.source



if __name__ == "__main__":

    list1 = [2.2, 4, 6]
    list2 = [3, 5, 7]
    v1 = Vector(list1)
    v2 = Vector(list2)

    print("Vector1", v1)
    print("Vector2", v2)

    distance = v1.distance(v2)
    dot = v1.dot(v2)

    print("distance between %s and %s is %s" % (v1, v2, distance))
    print("dot product between %s and %s is %s" % (v1, v2, dot))

    cross = v1.cross(v2)
    print("cross product between %s and %s is %s" % (v1, v2, cross))
    print("Is a Vector? ", isinstance(cross, Vector))
