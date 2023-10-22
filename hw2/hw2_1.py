import random
import math
from math import e
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

def simulation_one_avg(cast_time): 
    all_obtain = []
    all_x = []
    sum = 0
    for i in range(cast_time):
        x = random.uniform(-2,2)
        all_x.append(x)
        first = (x+(x**2))
        obtain = e**first
        all_obtain.append(obtain)
        sum = sum + obtain
        # print(obtain)

    # fig = plt.figure()
    # plt.xlabel('limited x')
    # plt.ylabel('obtained random nmber')

    # # y_major_locator = MultipleLocator(0.5)
    # # ax=plt.gca()
    # # ax.yaxis.set_major_locator(y_major_locator)
    # plt.xlim(-3,3)
    # plt.bar(all_x,all_obtain,0.01)
    # # fig.show()
    # fig.savefig('test.png',dpi=500)

    return round(sum/cast_time,5)

def show_figure(Trail_N_times,name):
    y = Trail_N_times
    x = list(range(1,11))
    print(y)
    fig = plt.figure()
    plt.xlabel('nth trail')
    plt.ylabel('Average')
    plt.bar(x,y)
    # plt.show()
    fig.savefig('result of trail ' + str(name) + " times " + '.png',dpi=500)


def main():
    Trail_10times = []
    Trail_100times = []
    Trail_1000times = []
    Trail_10000times = []
    Trail_100000times = []

    for i in range(10):
        Trail_10times.append(simulation_one_avg(10)*4)
        Trail_100times.append(simulation_one_avg(100)*4)
        Trail_1000times.append(simulation_one_avg(1000)*4)
        Trail_10000times.append(simulation_one_avg(10000)*4)
        Trail_100000times.append(simulation_one_avg(100000)*4)



    show_figure(Trail_10times,10)
    show_figure(Trail_100times,100)
    show_figure(Trail_1000times,1000)
    show_figure(Trail_10000times,10000)
    show_figure(Trail_100000times,100000)


simulation_one_avg(10000)

main()





    




    