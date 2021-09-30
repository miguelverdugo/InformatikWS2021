"""
Exercise 01: Simple calculator
"""

import time
import numpy as np

def Ex_01():
    user_input = ""

    while user_input != "stop":
        user_input = input("Enter a number (enter \"stop\" to end the programm)")
        if user_input == "stop":
            continue
        else:
            var_1 = float(user_input)
        operator = input("Please enter an operator (+, -, *, /):")

        var_2 = float(input("Please enter the second number:"))

        if operator == "+":
            print(var_1, "+", var_2, "=", var_1+var_2)
        elif operator == "-":
            print(var_1, "-", var_2, "=", var_1-var_2)
        elif operator == "*":
            print(var_1, "*", var_2, "=", var_1*var_2)
        elif operator == "/":
            print(var_1, "/", var_2, "=", var_1/var_2)
        else:
            print("Operator not supported!")
    return

"""
Exercise 02: State Machine
"""

def Ex_02(mode="for"):
    color = "green"
    if mode == "for":
        for i in range(5):
            if color == "red":
                color = "green"
                print(color)
                time.sleep(2)
            elif color == "green":
                color = "red"
                print(color)
                time.sleep(4)
    elif mode == "while":
        while True:
            if color == "red":
                color = "green"
                print(color)
                time.sleep(2)
            elif color == "green":
                color = "red"
                print(color)
                time.sleep(4)
    else:
        print("Mode not supported!")
    return

"""
Exercise 03: Unit converter
"""

def Ex_03():
    distance = float(input("Please enter the distance in LJ: "))

    distance_km = distance * 9.46e12

    distance_pc = distance * 0.306
    exponent = np.floor(np.log10(distance_km))
    print("Distance in km:", distance_km/(10**exponent), "*10^", exponent)

    if distance_pc > 1e9:
        print("Distance in pc:", distance_pc/1e9, "Gpc")
    elif distance_pc > 1e6:
        print("Distance in pc:", distance_pc/1e6, "Mpc")
    elif distance_pc > 1e3:
        print("Distance in pc:", distance_pc/1e3, "kpc")
    else:
        print("Distance in pc:", distance_pc, "pc")

    return

"""
Exercise 04: String Inversion
"""

def Ex_04():
    word = input("Please enter a string: ")
    output = ""
    for i in range(len(word), 0, -1):
        output = output + word[i-1]
    print(output)

    return

"""
Exercise 05: Distance between two points
"""

def Ex_05():
    l1 = [2.8, -4.7, 0.4]
    l2 = [-8.1, 3.0, -10.6]

    sum = 0

    for i in range(len(l1)):
        sum = sum + (l1[i]-l2[i])**2

    sum = np.sqrt(sum)

    print("The distance is", sum)

    return

if __name__ == "__main__":
    #Ex_01()
    #Ex_02()
    #Ex_03()
    #Ex_04()
    Ex_05()
