# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

# Exercise sheet 3 - Python basics and Data types

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Start a `python` shell and type

    ```python
    import this
    ```
   Explain what you are doing and the result.


2. Create a `jupyter` notebook and use it to explain the most important `python` data types
   (e.g. `str`, `int`, `float`, `list`, `dict`, `tuple`, etc)

       - How do you determine the type of a variable?


3.  Write a `python` script that takes 3 numbers as command line arguments, adds them up and prints
    the result. Access to the command line arguments is provided by the module `sys`, where `sys.argv[n]` represents the argument at the `n` position.


4. The function ``sys.getsizeof(object)`` returns the size (in bytes) of a ``python`` object in memory.
   According to that function, How much memory a _float_ uses **in** ``python``? Please explain the difference
   with respect to the the system requirements.


5. Write a Python script that takes a string as a command-line argument and reverses the order of the letters and
   calculates its entropy.


6. Write a simple python script that takes a distance in lightyears and returns
   that distance in both parsec and kilometers. In the case of parsec, the script
   should return the proper SI notation (e.g. Gpc, Mpc, kpc depending on the distance).
   The distance in kilometers shall be written in proper scientific notation.
