Informatics for Astronomers - WS2020
====================================

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Gerald Mösenlechner**

Exercise sheet 9 - Python classes, HTML & SQL
=============================================

------------------------------------------------------------------------

> *The following will be also part of the assessment:*
>
> *(1) Try to present exercises in a way that everyone can understand
> (even those who didn't do the exercises), so please explain the vital
> parts of your solution in a clear way.*
>
> *(2) Try to also include some background information where applicable,
> and/or explain the possible context/motivation for the given
> exercise.*

------------------------------------------------------------------------

1.  Consider a `class` that defines a circumference.

    ``` {.python}
    class Circle:
        def __init__(self, radius):
            self.radius = radius   
    ```

    Besides radius, a circumference should have attached the following
    properties/attributes that derive from the radius:

    -   perimeter
    -   area

    Please implement them (there are a few ways to do it). Save the the class in a `.py` file and import it
    from another (or from a `Jupyter notebook`) and show how the class works by doing a few calculations.  

2.  In Exercise 6, question 2, you created functions to calculate the
    distance, the dot and cross products of vectors. Please transform
    these functions into class methods of a new class `Vector` so we can
    perform the following operations as:

    ``` {.python}

    v1 = Vector(list1)
    v2 = Vector(list2)

    value1 = v1.distance(v2)  # a float
    value2 = v1.dot(v2)       # another float

    v3 = v1.cross(v2)         # another Vector check with
    isinstance(v3, Vector)
    > True
    ```

3. Stars are very important astrophysical objects whose main properties and subsequent
   evolution are determined at the time of birth.
   Please structure the skeleton of a class that describe a star at any point during
   its evolution. _Do not implement any actual calculation_. The purpose of the exercise
   is to think how to structure `python classes`. The class should look like that,

    ``` {.python}
    class Star:
        def __init__(self, parameters):

            # Important attributes

        def method1(self, some_parameters):
            return result1

        def method2(self, other_parameters):
            return result2     

    # Etc    
    ```

    Think about which are parameters necessary to initialize the class or
    from an astrophysical perspective, the most fundamental property (-ies) of a star that determine
    the rest of their characteristics. Sketch those characteristics as attributes, methods and properties.

4.  Please create (with an editor) a simple webpage that includes some
    pictures, text and links to your favorite website.

    -   Open the webpage with your browser and show us the source.

    -   Now go to <http://www.google.com> and show us the source code.

    Opinions?

5.  The Sloan Digital Sky Survey has produced catalogs of millions of
    objects on the sky. These catalogs are stored in `SQL` databases and
    are easily accessible through their webpages.

    For example,
    <http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx> allows
    to search of objects within a certain distance from the central
    position. In reality that web page execute a `SQL` command, which is
    also shown along the results of the query.

    Using the `SQL` form
    <http://skyserver.sdss.org/dr15/en/tools/search/sql.aspx> is
    possible to execute arbitrary queries. Copy the previous command
    here and execute it again. Play a bit with the parameters.

    -   What is the advantage of the "pure" `SQL` form in comparison
        with the radial form used at the beginning?

    -   What do you think about the `SQL` syntax?

    -   Is possible to access `SQL` databases with `python`?
