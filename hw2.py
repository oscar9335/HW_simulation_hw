import random
import math
from math import e

def simulation_one_avg(cast_time): 
    sum = 0
    for i in range(cast_time):
        x = random.uniform(-2,2)
        first = (x+(x**2))
        obtain = e**first
        sum = sum + obtain
        # print(obtain)
    return sum/cast_time


Trail_10times = []
Trail_100times = []
Trail_1000times = []
Trail_10000times = []
Trail_100000times = []

for i in range(10):
    Trail_10times.append(simulation_one_avg(10)*4)
    Trail_100times.append(simulation_one_avg(100)*4)
    Trail_1000times.append(simulation_one_avg(1000)*4)
    Trail_10000times.append(simulation_one_avg(10000)*4)
    Trail_100000times.append(simulation_one_avg(100000)*4)

print(Trail_10times)
print(Trail_100times)
print(Trail_1000times)
print(Trail_10000times)
print(Trail_100000times)


    




    