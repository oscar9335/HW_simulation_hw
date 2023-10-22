# A simulation : a dice with number from 1~6, every number has the same opportunity to be rolled, 
# the Expectation is 1+2+3+4+5+6/6 = 3.5

import csv
# B simulation : a dice with number from 1~6, 1 has 1/21 of probability to be rolled, 2 has 2/21,
#3 has 3/21, 4 has 4/21, 5 has 5/21, 6 has 6/21. the Expectation is 91/21
import random

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

A_dice = [1,2,3,4,5,6]
B_dice = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]

def A_simulation():
    graphs = [10,50,100,1000]
    numbers = []
    average = []

    for i in range(1000):
        numbers.append(random.choice(A_dice))


    for x in range(1000):
        if x == 0:
            average.append(numbers[0])
        else:
            full = 0
            for j in range(x+1):
                full = full + numbers[j]
            avg = full / (x + 1)
            average.append(avg)

            if(x == 9):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average')
                plt.xlim(0,10)

                y_major_locator = MultipleLocator(0.5)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)
                plt.ylim(1,6)
                plt.plot([j for j in range(1,11)],average)
                # fig.show()
                fig.savefig('result' + 'of' + str(10) + " times simulation" + '.png',dpi=500)
            if(x == 49):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average')
                plt.xlim(0,50)

                y_major_locator = MultipleLocator(0.5)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)
                plt.ylim(1,6)
                plt.plot([j for j in range(1,51)],average)
                # fig.show()
                fig.savefig('result' + 'of' + str(50) + " times simulation" + '.png',dpi=500)
            if(x == 99):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average')
                plt.xlim(0,100)

                y_major_locator = MultipleLocator(0.5)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)
                plt.ylim(1,6)
                plt.plot([j for j in range(1,101)],average)
                # fig.show()
                fig.savefig('result' + 'of' + str(100) + " times simulation" + '.png',dpi=500)
            if(x == 999):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average')
                plt.xlim(0,1000)

                y_major_locator = MultipleLocator(0.5)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)
                plt.ylim(1,6)
                plt.plot([j for j in range(1,1001)],average)
                # fig.show()
                fig.savefig('result' + 'of' + str(1000) + " times simulation" + '.png',dpi=500)

def B_simulation(pickanumform1_6):
    numbers = []
    possibility = []
    average_pro = []

    for i in range(1000):
        numbers.append(random.choice(B_dice))

    for i in range(1000):
        if numbers[i] != pickanumform1_6:
            possibility.append(0)
        else:
            possibility.append(1)
    
    for i in range(1000):
        if i == 0:
            average_pro.append(possibility[0])
        else:
            full = 0
            for j in range(i):
                full = full + possibility[j]
            avg = full / (1 + i)
            average_pro.append(avg)

            if(i == 9):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average probability')
                plt.xlim(1,10)

                y_major_locator = MultipleLocator(0.05)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)

                plt.ylim(0,1)
                plt.plot([i for i in range(1,len(average_pro)+1)],average_pro)
                # fig.show()
                fig.savefig('pro_result' + 'of' + str(10) + " times simulation for" + str(pickanumform1_6) + '.png',dpi=500)
            if(i == 49):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average probability')
                plt.xlim(1,50)

                y_major_locator = MultipleLocator(0.05)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)

                plt.ylim(0,1)
                plt.plot([i for i in range(1,len(average_pro)+1)],average_pro)
                # fig.show()
                fig.savefig('pro_result' + 'of' + str(50) + " times simulation for" + str(pickanumform1_6) + '.png',dpi=500)
            if(i == 99):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average probability')
                plt.xlim(1,100)

                y_major_locator = MultipleLocator(0.05)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)

                plt.ylim(0,1)
                plt.plot([i for i in range(1,len(average_pro)+1)],average_pro)
                # fig.show()
                fig.savefig('pro_result' + 'of' + str(100) + " times simulation for" + str(pickanumform1_6) + '.png',dpi=500)


            if(i == 999):
                fig = plt.figure()
                plt.xlabel('Number of trials')
                plt.ylabel('Average probability')
                plt.xlim(1,1000)

                y_major_locator = MultipleLocator(0.05)
                ax=plt.gca()
                ax.yaxis.set_major_locator(y_major_locator)

                plt.ylim(0,1)
                plt.plot([i for i in range(1,len(average_pro)+1)],average_pro)
                # fig.show()
                fig.savefig('pro_result' + 'of' + str(1000) + " times simulation for" + str(pickanumform1_6) + '.png',dpi=500)

    



A_simulation()
B_simulation(6)
B_simulation(3)
