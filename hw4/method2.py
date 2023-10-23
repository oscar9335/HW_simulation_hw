import random
import math
import matplotlib.pyplot as plt
import numpy as np

def generate_unordered_poisson_arrival_times(rate, T):
    arrival_times = []

    while(sum(arrival_times)) < T:
        U = random.random()
        t = -(1 / rate) * math.log(U)   # from method 1
        if t <= T:
            arrival_times.append(t)

    # arrival_times.sort()

    return arrival_times

# Example usage:
rate = 10.0  # Adjust the rate as needed
T = 1.0   # Adjust the time period as needed

print(len(generate_unordered_poisson_arrival_times(rate, T)))

number_events = []
for i in range(1000000):
    poisson_process = generate_unordered_poisson_arrival_times(rate, T)
    number_events.append(len(poisson_process))

unique, counts = np.unique(number_events, return_counts=True)

a_dict = dict(zip(unique, counts))

# print(a_dict)
print(max(a_dict,key=a_dict.get))
fig = plt.figure()
plt.xlabel('Number of events')
plt.ylabel('Number of events corresponding probability')
plt.plot(unique, counts/1000000,marker = 'o')
plt.show()
fig.savefig('method 2 generate_unordered_poisson_arrival_times plot with rate = 10.0' + '.png',dpi=500)
