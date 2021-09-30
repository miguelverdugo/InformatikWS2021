# Informatics for Astronomers - WS2020

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Gerald Mösenlechner**

# Exercise sheet 7 - Bash and Fortran

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---


1. Take the `python` calculator from Exercise 04, Example 1 and implement it as a `bash` script.

2. Take the file `Photomety_V_Band.txt`. This file contains photometric and positional data of over 6000 stars. The first column contains the ID of the stars, the second and third contain the `X` and `Y` position and the fourth column contains the flux in ADU (Analog-Digital Units). Use `awk` to select all stars in a $500\times 500$px$^2$ around the center (1000, 1000) and write the result to a new file. Then sort the file based on the flux.

3. Write the result from pythons "`import this`" into a .txt file (how you do this is up to you). Then use the `sed` command line tool to search and replace a word of your choosing with a different one and save the result to a new file.

4. Write a simple shell script that takes the `Photomety_V_Band.txt` and counts the number of stars inside of a 300px radius around the center (1000,1000). The script shall then print the resulting number and the ID and signal of the brigthest star inside of that region.

5. Write a `Fortran` program that uses the Babylonian Method to calculate the approximate square root of 42.
