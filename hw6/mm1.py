import numpy as np
import random

def mm1_queue(lambda_possion,customers,lambda_service):
    waiting_time = []
    customer_arraival_time_timeline = []
    all_service_time = []
    this_service_time = 0

    for i in range(customers): # how many service I want to count

    # A customer arrive ---------------------------------------------------------------------------------------------
        this_arrival_time = -np.log(random.uniform(0,1))/lambda_possion   # possion arrival
        if not customer_arraival_time_timeline:
            customer_arraival_time_timeline.append(this_arrival_time)
        else:
            customer_arraival_time_timeline.append(customer_arraival_time_timeline[-1] + this_arrival_time)

    # check if this customer need to wait ---------------------------------------------------------------------------
        if len(customer_arraival_time_timeline) == 1:
            waiting_time.append(0)
        elif customer_arraival_time_timeline[-1] < customer_arraival_time_timeline[-2] + this_service_time:
            # the previous service not done when this new customer arrive 
            waiting_time.append(customer_arraival_time_timeline[-2] + this_service_time - customer_arraival_time_timeline[-1])
        else:
            # this new customer do not have to wait
            waiting_time.append(0)

    # serving this customer -----------------------------------------------------------------------------------------
        this_service_time = -np.log(random.uniform(0,1))/lambda_service  # exponential distribution
        all_service_time.append(this_service_time)


    return customer_arraival_time_timeline,waiting_time,all_service_time




arrival, wait, service_timne = mm1_queue(lambda_possion= 2,customers = 10,lambda_service = 1)

print(arrival)
print(service_timne)

utilization = sum(service_timne)/(arrival[-1] + wait[-1] + service_timne[-1])

print(utilization)





