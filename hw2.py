import random
import math
from math import e

def simulation_one(cast_time):
    for i in range(cast_time):
        x = random.uniform(-2,2)
        first = (x+x**2)
        obtain = e**first
        print(obtain)

simulation_one(5)


    