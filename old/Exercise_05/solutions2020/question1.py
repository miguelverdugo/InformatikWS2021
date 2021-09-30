

def distance(vec1, vec2):
    """
    returns the distance between to vectors


    Parameters
    ----------
    vec1 : list-like
        vector1
    vec2 : list like
        vector2

    Returns
    -------
    float, 
    distance between these to vectors, 

    """
    dist = sum([(x - y)**2 for x, y in zip(vec1, vec2)])**0.5
    
    return dist


def dot(vec1, vec2):
        """
        returns the dot product of two vectors
        """
        result = sum([x*y for x, y in zip(vec1, vec2)])

        return result
    
def cross(vec1, vec2):
        """
        returns the cross product of two vectors
        """
        a1, a2, a3 = vec1
        b1, b2, b3 = vec2
        result = [a2*b3 - a3*b2,
                  a1*b3 - a3*b1,
                  a1*b2 - a2*b1]

        return result
    

    
if __name__ == "__main__":
    
    point_1 = [2.8, -4.7, 0.4]
    point_2 = [-8.1, 3.0, -10.6]
    
    print("Vector1:", point_1)
    print("Vector2:", point_2)
    print("Distance between these vectors is", distance(point_1, point_2))
    print("Dot product between these vectors is", dot(point_1, point_2))
    print("Cross product between these vectors is", cross(point_1, point_2))
    
    
    