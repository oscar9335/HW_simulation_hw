import random
import math

def simulation_two(cast_times):
    sum = 0
    for i in range(cast_times):
        one_trail_sum = 0
        count = 0
        while(one_trail_sum <= 1):
            a = random.random()
            a = round(a,15)
            one_trail_sum = one_trail_sum + a
            count += 1
            # print(a)
        sum = sum + count
    return sum / cast_times

    

print(simulation_two(10))
print(simulation_two(100))
print(simulation_two(10000))
print(simulation_two(10000000))
