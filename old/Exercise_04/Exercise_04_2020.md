# Informatics for Astronomers - WS2020

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Gerald Mösenlechner**

# Exercise sheet 4 - Python If conditions and Loops

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---


1. Write a simple calculator that should prompt the user to enter two numbers
   using the `input()` function. The calculator should be able to add, subtract,
   multiply and divide. Try to implement it in a way where it can be used
   indefinitely for a single start of the program, until a certain command is given.

2. Take the traffic light state machine from the first lecture and try implement it as a python script
   that loops the cycle _n_ times (with a `for`-loop) and indefinitely (using a `while`-loop). Store
   the color of the light in a variable and check its current status before switching.

3. Write a simple python script that takes a distance in lightyears and returns
   that distance in both parsec and kilometers. In the case of parsec, the script
   should return the proper SI notation (e.g. Gpc, Mpc, kpc depending on the distance).
   The distance in kilometers shall be written in proper scientific notation.

4. Write a Python script that takes a string as a command-line argument and reverses the
   order of the letters.

5. Assume that these two lists are 3D coordinates:

    ```python
    point_1 = [2.8, -4.7, 0.4]
    point_2 = [-8.1, 3.0, -10.6]
    ```
  
   Write a script that computes the distance between those points
   (by looping over the individual components)


