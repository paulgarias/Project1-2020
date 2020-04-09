import pandas as pd 
import numpy as np 

def show_message(name):
    print(f"Hello, {name}!")

def get_random(num):
    return np.random.randint(0,5,10)

show_message("Paul")
