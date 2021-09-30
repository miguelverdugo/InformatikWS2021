#  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 3 - Linux and scripts

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

1. What are the `man` pages? Execute `man <command>` and explain its contents. 

2. What are (file) links in linux? How do you create them? Pleas show an example. What is the difference between "hard" and
"soft" links? How do you know if a file is a link?

3. How can you find a file in your disk and determine its type in a single command line? 
Hint: use `find`/`locate`, `|` and `xargs`

4. How do you set alias, environmental variables, etc in Linux? What are they useful for? 

 5. If you are using ``bash`` as a linux shell you will find a file in your home directory called ``.bashrc`` 
   (and/or ``.bash_profile``). Explain its contents. 
  
6.  Consider at the following simple bash script.
 
    ```bash
        #!/bin/bash
        # usage sum.sh integer1 integer2
        echo Thiking a bit
        sleep 2
        ((sum=$1+$2))
        echo $sum
    
    ```
    * Please explain its contents. 
    * Copy  it to your system and execute it.
    * Modify the operation (changing `+` by `-`, etc) and see what happens.   
