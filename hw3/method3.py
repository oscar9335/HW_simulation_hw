import random
import math
import numpy as np
import matplotlib.pyplot as plt

def geometric_random_generator_log(p):
    u = random.random()  # Generate a uniform random number between 0 and 1
    q= 1-p
    x = math.ceil(math.log(u) / math.log(q))  # 實作inverse transform 公式 取math.log(u) / math.log(q)整數後+1
    return x


p = 0.005  # Probability of success
result = []
for i in range(1000000):
    result.append(geometric_random_generator_log(p))


unique, counts = np.unique(result, return_counts=True)
# print("各數字出現次數：", dict(zip(unique, counts)))

plt.figure(figsize = (20, 10))
p1 = plt.bar(unique, counts, width= 0.35)
# plt.bar_label(p1, label_type='edge')
plt.xlabel("Generated number")
plt.ylabel("how many times it appeard")
plt.title("log method generator result with P = 0.1")
plt.show()


# time complexity on math.ceil(math.log(u) / math.log(q)) is O(14)
# the total time complexity depends on how many number I want to generate so = O(n)