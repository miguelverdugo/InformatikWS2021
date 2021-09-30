  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 8 - Python classes, etc.

---

> _Your preparation of exercises should include two aspects:_
>
> _(1) Try to present exercises in a way that everyone can follow (even if that
> person didn’t do the exercise at all), so please explain all the (vital) parts of
> your solution in a slow and comprehensive way._
>
> _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._
>
---

1. Please find out a list of built-in exceptions (errors) in python and their meaning. For a few, show
   (with examples) when and how they occur.  


2. Consider a ``class`` that defines a circumference.

   ````python

   class Circle:
       def __init__(self, radius):
           self.radius = radius   

   ````

    Besides radius, a circumference should have attached the following properties/attributes that
    derive from the radius:

   - perimeter
   - area

   Please implement them and show how they work. There are a few ways to do it.

3. In Exercise 5, question12, you created functions to calculate the distance, the dot and cross products
   of vectors. Please transform these functions into class methods of a new class ``Vector`` so we can
   perform the following operations as:

   ````python

   v1 = Vector(list1)
   v2 = Vector(list2)
   value1 = v1.distance(v2)  # a float
   value2 = v1.dot(v2)       # another float
   v3 = v1.cross(v2)         # another Vector check with
   isinstance(v3, Vector)
   > True

   ````

4. Which other operations are still necessary to implement to make the ``class Vector`` fully functional?
   Please structure an skeleton of the class, that is, do not implement these operations/methods yet, just
   write them down as following:

   ````python

   class Vector:
       def __init__(self, vector):
           self.some_attribute = attribute
           # Etc
       def method1(self, some_parameter):
           pass

       def method2(self, another_parameter):
           pass
       # Etc   

   ````

   - Save that ``class`` in some text file (.py) and import it from a different one.

5. Please go to http://pypi.org and look for a python package of your preference. You can either
download it or go to the project webpage (typically in ``github.org``) to see the package contents.
Please explain the structure of the package and the function of the different files.
