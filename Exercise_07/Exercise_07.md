# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

# Exercise sheet 7 - Python classes

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Consider a ``class`` that represents a circumference.

    ````python

    class Circle:
        def __init__(self, radius):
            self.radius = radius   

    ````

    Besides radius, a circumference should have attached the following properties/attributes that are
    derived from the radius:

    - perimeter
    - area

    Please implement them and show how they work. There are a few ways to do it.

2. During the tutorium, functions to calculate the distance between vectors and the dot ($\cdot$) and the cross ($\times$)
   products were implemented. Please transform these functions into class methods of a new class ``Vector`` so we can perform the following operations as:

    ````python

    list1 = [-2.4, 0.1, 5.3]
    list2 = [4.7, -3.0, 1.7]

    v1 = Vector(list1)
    v2 = Vector(list2)
    value1 = v1.distance(v2)  # a float
    value2 = v1.dot(v2)       # another float
    v3 = v1.cross(v2)         # another Vector check with
    isinstance(v3, Vector)
    > True

    ````

3.  Please create (with an editor) a simple webpage that includes some
    pictures, text and links to your favorite website.

    - Open the webpage with your browser and show us the source.

    - Now go to <http://www.google.com> and show us the source code.

     Opinions?

4.  The Sloan Digital Sky Survey has produced catalogs of millions of
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


5.


6. 
