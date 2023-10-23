import random
import numpy as np
import matplotlib.pyplot as plt  

def geometric_random_generator_qp(p):
    trials = 0
    while True:
        trials += 1
        if random.random() <= p:
            return trials

p = 0.005  # Probability of success
result = []
for i in range(1000000):
    result.append(geometric_random_generator_qp(p))


unique, counts = np.unique(result, return_counts=True)
# print("各數字出現次數：", dict(zip(unique, counts)))
a_dict = dict(zip(unique, counts))

plt.figure(figsize = (20, 10))
p1 = plt.bar(unique, counts, width= 0.35)
# plt.bar_label(p1, label_type='edge')
plt.xlabel("Generated number")
plt.ylabel("how many times it appeard")
plt.title("P Q method generator result with P = 0.1")
plt.show()

print(max(a_dict,key=a_dict.get))


# print(f"Number of trials until success: {result}")
# ex 武漢肺炎確診率是0.05，今天測試一台境外移入飛機，直到驗出確診的次數

# time complexity on geometric_random_generator_qp O(1/p) = O(1)
# the total time complexity depends on how many number I want to generate so = O(n)