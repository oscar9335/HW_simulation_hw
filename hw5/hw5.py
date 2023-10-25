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

def generate_second_translation(limit = False):
    score_z = generate_first()
    score = score_z*5 + 70
    if(limit == True):
        while( score < 0 or score > 100):
            score_z = generate_first()
            score = score_z*5 + 70

    return score

def empirical_rule(a_list):
    fig = plt.figure()
    # Create a histogram
    plt.hist(a_list, bins='auto', density=True, alpha=0.5, color='b', edgecolor='black')
    plt.xlabel('X-Axis')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normally Distributed Data')

    # Calculate mean and standard deviation of the data
    mean = np.mean(a_list)
    std_dev = np.std(a_list)

    # Draw lines for the 68-95-99.7 empirical rule
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)
    plt.plot(x, 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2), color='r', linewidth=2, label='PDF')
    # plt.axvline(mean, color='g', linestyle='dashed', linewidth=2, label='Mean')
    plt.axvline(mean - std_dev, color='m', linestyle='dashed', linewidth=2, label='1 Standard Deviation')
    plt.axvline(mean + std_dev, color='m', linestyle='dashed', linewidth=2)
    plt.axvline(mean - 2 * std_dev, color='c', linestyle='dashed', linewidth=2, label='2 Standard Deviations')
    plt.axvline(mean + 2 * std_dev, color='c', linestyle='dashed', linewidth=2)
    plt.axvline(mean - 3 * std_dev, color='y', linestyle='dashed', linewidth=2, label='3 Standard Deviations')
    plt.axvline(mean + 3 * std_dev, color='y', linestyle='dashed', linewidth=2)

    # Add a legend
    plt.legend()

    # Display the plot
    plt.show()

    fig.savefig("empirical rule hist" + ".png" ,dpi=500)


def plot_hist(a_list,name,Q = False):
    # plt.figure(figsize = (20, 10))
    fig = plt.figure()
    if Q == True:
        plt.hist(a_list,bins='auto',density=True,range=(-10, 110))
    else:
        plt.hist(a_list,bins='auto',density=True)
    plt.xlabel("X")
    plt.ylabel("density")
    plt.title("")
    plt.show()
    fig.savefig(name+ ".png" ,dpi=500)



all_X = []
for i in range(100000):
    all_X.append(generate_first())

all_Score = []
for i in range(100000):
    all_Score.append(generate_second_translation(True))

empirical_rule(all_Score)

# plot_hist(all_X,"Generate standard normal random variable revise from 5f  ")

# plot_hist(all_Score,"Generate standard normal random variable revise from 5f using translation ",True)
