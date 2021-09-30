from example1 import Vector
import numpy as np

class TestVector:

    def test_distance(self):
        v1 = Vector([1, 0, 0])
        v2 = Vector([-1, 0, 0])

        assert v1.distance(v2) == 2

    def test_distance(self):

        v1 = Vector(np.random.uniform(low=-10, high=10,  size=3))
        v2 = Vector(np.random.uniform(low=-10, high=10,  size=3))

        assert v1.distance(v2) == v2.distance(v1)

    def test_dot(self):

        v1 = Vector(np.random.uniform(low=-10, high=10,  size=3))
        v2 = Vector(np.random.uniform(low=-10, high=10,  size=3))

        assert v1.dot(v2) == v2.dot(v1)

    def test_cross(self):

        v1 = Vector(np.random.uniform(low=-10, high=10,  size=3))
        v2 = Vector(np.random.uniform(low=-10, high=10,  size=3))

        v3 = v1.cross(v2)
        v4 = v2.cross(v1)

        assert v3[1] == -1*v4[1]

    def test_cross_instance(self):

        v1 = Vector(np.random.uniform(low=-10, high=10,  size=3))
        v2 = Vector(np.random.uniform(low=-10, high=10,  size=3))

        v3 = v1.cross(v2)

        assert isinstance(v3, Vector)
