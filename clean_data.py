import pandas as pd 
import numpy as np 

def show_message(name, greet="Hello"):
<<<<<<< HEAD
    if greet=="hello":
=======
    if greet=="Hello":
>>>>>>> message_functions
        print(f"Hello, {name}!")
    elif greet=="goodbye":
        print(f"Goodbye, {name}!")

import math 
def show_factorial(num):
    print(f"Factorial of {num} is {math.factorial(num)}")

show_message("Paul")
show_factorial(5)
