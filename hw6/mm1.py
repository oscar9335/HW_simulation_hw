import numpy as np
import random
import matplotlib.pyplot as plt

def mm1_queue(lambda_possion,customers,lambda_service):
    waiting_time = []
    customer_arraival_time_timeline = []
    all_service_time = []
    customer_leave_time = []
    customer_waiting_queue =[]
    this_service_time = 0
    busy_flag = False

    for i in range(customers): # how many service I want to count
    # All customer ---------------------------------------------------------------------------------------------
        # arrive time
        this_arrival_time = -np.log(random.uniform(0,1))/lambda_possion   # possion arrival
        if not customer_arraival_time_timeline:
            customer_arraival_time_timeline.append(this_arrival_time)
        else:
            customer_arraival_time_timeline.append(customer_arraival_time_timeline[-1] + this_arrival_time)    

        # service time
        this_service_time = -np.log(random.uniform(0,1))/lambda_service
        all_service_time.append(this_service_time)
        waiting_time.append(0)

    # count wait time and leave time----------------------------------------------------------------------------
    for i in range(customers):   
        if i == 0:
            customer_leave_time.append(customer_arraival_time_timeline[i] + all_service_time[i])
        else:
            if(customer_leave_time[i-1] > customer_arraival_time_timeline[i]):
                waiting_time[i] = customer_leave_time[i-1] - customer_arraival_time_timeline[i]
            else:
                waiting_time[i] = 0
            customer_leave_time.append(waiting_time[i] + customer_arraival_time_timeline[i] + all_service_time[i])





    return customer_arraival_time_timeline,waiting_time,all_service_time,customer_leave_time




arrival, wait, service_timne, leave = mm1_queue(lambda_possion= 1, customers = 1000,lambda_service = 1)

# print(arrival)
print(wait)
# print(service_timne)
# print(leave)

# utilization 
utilization = sum(service_timne)/(arrival[-1] + wait[-1] + service_timne[-1])
# waiting time
avg_waiting = sum(wait)/1000


print(utilization)
print(avg_waiting)

customers = [ i for i in range(1, 1000 + 1)]

fig = plt.figure()
plt.bar(customers,wait)
plt.xlabel('Customer number')
plt.ylabel('waiting time')
plt.title('customer and corresponding waiting time')
plt.show()
fig.savefig("customer and corresponding waiting time 1000 customer arrival time equal than service time" + ".png" ,dpi=500)




