import random
import math

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

# Example usage:
rate = 2.0  # Adjust the rate as needed
T = 10.0   # Adjust the time period as needed
poisson_process = generate_poisson_process(rate, T)
print("Poisson process events:", poisson_process)
print("Number of events:", len(poisson_process))