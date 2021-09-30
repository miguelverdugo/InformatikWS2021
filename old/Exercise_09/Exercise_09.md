  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 9 - Documentation, quality control and misc

---

> _Your preparation of exercises should include two aspects:_
>
> _(1) Try to present exercises in a way that everyone can follow (even if that
> person didn’t do the exercise at all), so please explain all the (vital) parts of
> your solution in a slow and comprehensive way._
>
> _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Please write the docstrings for our class ``Vector`` and its implemented methods (distance,
   dot and cross products).  

    - Please show the most common formats (``numpydoc``, ``google`` and ``reST``) and
    discuss their differences.

    - How do you access the doctrings within in a ``python`` session?

2. Write some simple tests for our class ``Vector``. A test suite should look like

   ````python
   class TestVector:

       def test_method1(self):
            assert "condition"

       def test_method2(self):
            assert "another condition"        
   ````
   (a test suite can be executed with the following command: ``python -m pytest tests.py`` or simply ``pytest test_file.py``)

3. Testing is an important part in software development. Please discuss the differences between *unit testing*, *integration testing* and *compliance testing*.

4. Please create (with an editor) a simple webpage that includes some pictures, text and links to your favorite website.

    - Open the webpage with your browser and show us the source.

    - Now go to [http://www.google.com](http://www.google.com) and show us the source code.

    Opinions?

5. The Sloan Digital Sky Survey has produced catalogs of millions of objects on the sky. These catalogs are stored in
   ``SQL`` databases and are easily accessible through their webpages. For example,
  [http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx](http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx) allows to search of objects within a certain distance
  from the central position. In reality that web page execute a ``SQL`` command, which is also shown
  along the results of the query.

   Using the ``SQL`` form [http://skyserver.sdss.org/dr15/en/tools/search/sql.aspx](http://skyserver.sdss.org/dr15/en/tools/search/sql.aspx)
   is possible to execute arbitrary queries. Copy the previous command here and execute it again.
   Play a bit with the parameters here.

    - What is the advantage of the "pure" ``SQL`` form in comparison with the radial form used at
      the beginning?

    - What do you think about the ``SQL`` syntax?

    - Is possible to access ``SQL`` databases with ``python``?
