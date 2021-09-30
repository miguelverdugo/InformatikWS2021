Informatics for Astronomers - WS2020
====================================

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Gerald Mösenlechner**

Exercise sheet 10 - Documentation and Testing
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

1. Please write the docstrings for our class ``Vector`` and its implemented methods (distance,
   dot and cross products).  

    - Please show the most common formats (``numpydoc``, ``google`` and ``reST``) and
    discuss their differences.

    - How do you access the doctrings within a ``python`` session?

2. Write some simple tests for our class ``Vector``. A test suite should look like

   ````python
   class TestVector:

       def test_method1(self):
            assert "condition"

       def test_method2(self):
            assert "another condition"        

       #etc
   ````
   (a test suite can be executed with the following command: ``python -m pytest tests.py`` or simply ``pytest test_file.py``)

3. Testing is an important part in software development. Please discuss the differences between *unit testing*, *integration testing* and *compliance testing*.

4. Create a package from the ``Vector`` example. In order to do this, follow the guide found at
 [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/) and upload it to the [PyPI testserver](https://test.pypi.org/). Then you should download/install it using `pip` and use it in a small script.

5. Create a `README.md` (in markdown) file for the package `Vector`, where basic instructions how to use the package are included, like purpose, installation, requirements and examples. The code for these examples should be embedded in the text and displayed with code highlighting. You can test the document with [https://jbt.github.io/markdown-editor/](https://jbt.github.io/markdown-editor/) for example.

   These `README` files are very important to provide basic information in code repositories. Besides markdown, what other markup language is also used for that purpose?
