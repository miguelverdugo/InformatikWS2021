#  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 4 - Linux and scripts

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

1. Take the calculator script from last exercise and try to improve it. After you start 
   the script, it should prompt the user to select from a list of mathematical operators and 
   store the selection in a variable (use the 'read' command). It should then use if-conditionals 
   in order to return the correct result. You can look up the precise syntax if you’re not sure, 
   it’s something like:   
   
	```bash
		if [ "$CHOICE" == "y" ]; then
		...
		elif [ "$CHOICE" == "n" ]; then
		...
		else
		...
		fi
    
    ```

2. Look up the different classifications for state-machines. How do they differ?

3. Take the traffic light example from the lecture and try implement it as a bash script 
   that loops the cycle _n_ times (with a for-loop) and indefinitely (using a while-loop). Store 
   the color of the light in a variable and check its current status before switching.

4. Explain the difference between an interpreted and a compiled programing language.

5. What does the 'Global Interpreter Lock' do and why is it needed. What are its drawbacks. 
