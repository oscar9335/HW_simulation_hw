import random
import math

def generate_unordered_poisson_arrival_times(rate, T, n):
    arrival_times = []

    for _ in range(10):
        U = random.random()
        t = -(1 / rate) * math.log(U)
        if t <= T:
            arrival_times.append(t)

    arrival_times.sort()

    return arrival_times

# Example usage:
rate = 2.0  # Adjust the rate as needed
T = 10.0   # Adjust the time period as needed
n = 5     # Adjust the number of arrival times as needed

arrival_times = generate_unordered_poisson_arrival_times(rate, T, n)
print("Unordered Poisson arrival times:", arrival_times)