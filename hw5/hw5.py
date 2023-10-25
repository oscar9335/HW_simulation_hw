import math
import random
import numpy as np
import matplotlib.pyplot as plt  

def gen_Y_expo():
    return -math.log(random.uniform(0,1))

def generate_first():
    while(True):
        U = random.uniform(0,1)
        Y = gen_Y_expo()
        if U <= math.e**((-0.5*((Y-1)**2))):
            if random.random() > 0.5:
                X = Y
            else:
                X = -Y
            break

    return X

all_X = []

for i in range(100000):
    all_X.append(generate_first())

# print(all_X)



# plt.figure(figsize = (20, 10))
fig = plt.figure()
p1 = plt.hist(all_X,bins='auto',density=True)
plt.xlabel("X")
plt.ylabel("density")
plt.title("")
plt.show()
fig.savefig('question1'+ ".png" ,dpi=500)