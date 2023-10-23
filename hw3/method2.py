# brutal
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def geometric_random_generator_traditional(p):
    u = random.random()  # Generate a uniform random number between 0 and 1
    # print(u)
    q= 1-p
    trail = 0
    
    while True:
        trail += 1 
        if 0 <= u < all_round[0]:
            return 1
        if len(all_round) <= trail:
            all_round.append(q * all_round[trail-1])
            # elif  sum(all_round[0:trail]) <= u <sum(all_round[0:trail+1]):
            #     print(sum(all_round[0:trail-1]))
            #     print(sum(all_round[0:trail]))
            #     print (trail-1)
            #     return trail-1
            # else:
            #     all_round.append( q * all_round[trail])
        if sum(all_round[0:trail-1]) <= u <sum(all_round[0:trail]):
            return trail



p = 0.005 # Probability of success
all_round = [p]

result = []
for i in range(1000000):
    result.append(geometric_random_generator_traditional(p))
# print (all_round)


unique, counts = np.unique(result, return_counts=True)
# print("各數字出現次數：", dict(zip(unique, counts)))

plt.figure(figsize = (20, 10))
p1 = plt.bar(unique, counts, width= 0.35)
# plt.bar_label(p1, label_type='edge')
plt.xlabel("Generated number")
plt.ylabel("how many times it appeard")
plt.title("tradtional method generator result with P = 0.1")
plt.show()


# time complexity in worst case is O(n)
# the total time complexity depends on how many number I want to generate so = O(n^2)