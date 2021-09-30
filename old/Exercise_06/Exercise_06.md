  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 6 - Python Basics and loops and C

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
> _Please strive for that in all exercises to come. From now on this will also be part of the assessment._

---

1. How are _floats_ represented in computer memory? (think of basis and exponent).
   How much memory does a _float_ need in the system?

2. The function ``sys.getsizeof(object)`` returns the size (in bytes) of a ``python`` object
   in memory. According to that function, How much memory a _float_ uses **in** ``python``? Please
   explain the difference with respect to the the system requirements.

3. Write a Python script that takes a string as a command-line argument and reverses the
   order of the letters.

4. Assume that these two lists are 3D coordinates:
   ```pyhton
   point_1 = [2.8, -4.7, 0.4]
   point_2 = [-8.1, 3.0, -10.6]
   ```
   Write a script that computes the distance between those points
   (by looping over the individual components)

5. Copy the result of ``import this`` into a text file. Open the file and 
   print each line.

   Perform also one (or all) of the following operations with the text:

    * Convert the text to upper case.
    * Print the number of characters in each line
    * Replace all single spaces with double ones.    

6. Write a simple ``C``-script that prints a message of your choice.

7. Bonus: Write questions 4. and 5. with both ``for`` and ``while`` loops. Explain
   the difference.
