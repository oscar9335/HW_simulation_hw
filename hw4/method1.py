import random
import math
import matplotlib.pyplot as plt
import numpy as np

def generate_poisson_process(rate, T):
    t = 0
    I = 0
    S = []

    while t < T:
        U = random.random()
        t -= (1 / rate) * math.log(U)

        if t > T:
            break

        I += 1
        S.append(t)

    return S


rate = 1.0  # Adjust the rate as needed
T = 1.0   # Adjust the time period as needed
number_events = []
for i in range(1000000):
    poisson_process = generate_poisson_process(rate, T)
    number_events.append(len(poisson_process))

unique, counts = np.unique(number_events, return_counts=True)
a_dict = dict(zip(unique, counts))
print(max(a_dict,key=a_dict.get))
fig = plt.figure()
plt.xlabel('Number of events')
plt.ylabel('Number of events corresponding counts')
plt.plot(unique, counts,marker = 'o')
plt.show()
fig.savefig('method 1 Number of events counting plot with rate = 1.0' + '.png',dpi=500)

