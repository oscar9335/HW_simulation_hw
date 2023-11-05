import numpy as np
import random

def mm1_queue(lambda_possion,customers,lambda_service):
    waiting_time = []
    customer_arraival_time_timeline = []
    customer_arraival_time_timeline.append(-np.log(random.uniform(0,1))/lambda_possion) # first customer
    busy_flag = False
    
    for i in range(customers-1): # how many service I want to count
        this_arrival_time = -np.log(random.uniform(0,1))/lambda_possion
        customer_arraival_time_timeline.append(customer_arraival_time_timeline[-1] + this_arrival_time)
        
        if busy_flag == True:

            pass
        else:
            this_service_time = -np.log(random.uniform(0,1))/lambda_service

    print(customer_arraival_time_timeline)


mm1_queue(1,10,1)            





