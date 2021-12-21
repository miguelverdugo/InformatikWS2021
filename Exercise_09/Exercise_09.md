# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

# Exercise sheet 8 -

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---
1. Please write the docstrings for our class ``Vector`` and its implemented methods (distance,
   dot and cross products) and access them within a `python` session.

2.  Please show the most common formats for docstrings (``numpydoc``, ``google`` and ``reST``) and
    discuss their differences using a example. That is, write the same doctring in the three formats.

3. Testing is an important part in software development. Please discuss the differences between *unit testing*, *integration testing* and *compliance testing*.

4. Write some simple tests for the class ``Vector``. That is, make sure that the methods are working as expected.

   ````python
   class TestVector:

       def test_method1(self):
            assert "condition"

       def test_method2(self):
            assert "another condition"        

       #etc
   ````
   (a test suite can be executed with the following command: ``python -m pytest tests.py`` or simply ``pytest test_file.py``)

5. Create a package containing the `class Vector`

6.
