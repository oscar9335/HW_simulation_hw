import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns  # Optional, for a nicer plot style
from scipy.stats import t

def mm1_queue(lambda_possion,customers,mu):
    waiting_time = []
    customer_arraival_time_timeline = []
    all_service_time = []
    customer_leave_time = []
    this_service_time = 0

    for i in range(customers): # how many service I want to count
    # All customer ---------------------------------------------------------------------------------------------
        # arrive time
        this_arrival_time = -np.log(random.uniform(0,1))/lambda_possion   # possion arrival
        if not customer_arraival_time_timeline:
            customer_arraival_time_timeline.append(this_arrival_time)
        else:
            customer_arraival_time_timeline.append(customer_arraival_time_timeline[-1] + this_arrival_time)    

        # service time
        this_service_time = -np.log(random.uniform(0,1))/mu
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

def mean_95percent_plot(wait):
    # Calculate mean and standard deviation
    mean_value = np.mean(wait)
    std_dev = np.std(wait)

    # random pick samples
    grouped_data = []
    num_groups = 15
    for i in range (num_groups):
        grouped_data.append(np.random.choice(wait, size=100, replace=False))
    # grouped_data = np.array_split(wait, num_groups)

    # Calculate means and confidence intervals for each group
    group_means = np.array([np.mean(group) for group in grouped_data])
    # group_std_devs = np.array([np.std(group) for group in grouped_data])
    group_conf_intervals = np.array([np.percentile(group, [2.5, 97.5]) for group in grouped_data])

    # Set the spacing between groups
    spacing = 40.0

    # Calculate the 95% confidence interval
    conf_interval = np.percentile(wait, [2.5, 97.5])

    # Plot the histogram
    sns.histplot(wait, kde=True, color='blue', edgecolor='black', label='Data')

    # Plot the means for each group
    plt.scatter(group_means, spacing + np.arange(num_groups) * spacing, color='red', marker='o', label='Group Means')


    # Plot the confidence intervals for each group
    for i in range(num_groups):
        plt.errorbar(group_means[i], spacing  + i * spacing, xerr=np.diff(group_conf_intervals[i])/2, color='red', fmt='none')


    # Add a vertical line for the mean
    plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean')

    # Add vertical lines for the confidence interval
    plt.axvline(conf_interval[0], color='green', linestyle='dashed', linewidth=2, label='95% CI')
    plt.axvline(conf_interval[1], color='green', linestyle='dashed', linewidth=2)

    # Add labels and title
    plt.xlabel('Waiting time ')
    plt.ylabel('Frequency')
    plt.title('Distribution with 95% Confidence Interval')

    # Show legend
    plt.legend()

    # Show the plot
    plt.show()

def average_wait_cal(wait):
    return sum(wait)/10000

def utiluzatio_cal(service_timne,arrival,wait):
    utilization = sum(service_timne)/(arrival[-1] + wait[-1] + service_timne[-1])   
    return utilization

def cal_confident_interval(wait):
    mean_value = np.mean(wait)
    a = np.percentile(wait, [2.5, 97.5])
    return a # a [xxx,xxx]

def mm1_queue_plot():
    # ... (your existing mm1_queue function)

    # Parameters
    num_simulations = 1000
    lambda_range = np.arange(0.01, 1.51, 0.01)
    mu_values = [0.25, 0.5, 1,2]

    mu_avg_wait_times = {mu: [] for mu in mu_values}
    mu_conf_intervals = {mu: [] for mu in mu_values}

    # Run simulations
    for mu in mu_values:
        for lambda_poisson in lambda_range:
            avg_wait_times = []
            for _ in range(num_simulations):
                _, waiting_times, _, _ = mm1_queue(lambda_poisson, 100, mu)
                avg_wait_times.append(np.mean(waiting_times))

            # Calculate confidence interval
            confidence_interval = t.interval(0.95, len(avg_wait_times) - 1,
                                            loc=np.mean(avg_wait_times),
                                            scale=np.std(avg_wait_times) / np.sqrt(len(avg_wait_times)))

            mu_avg_wait_times[mu].append(np.mean(avg_wait_times))
            mu_conf_intervals[mu].append(confidence_interval[1] - np.mean(avg_wait_times))

    # Plotting
    for mu, avg_wait_times in mu_avg_wait_times.items():
        conf_intervals = mu_conf_intervals[mu]
        # plt.errorbar(lambda_range, avg_wait_times, yerr=conf_intervals, label=f'mu={mu}')
        plt.plot(lambda_range, avg_wait_times, label=f'mu={mu}')
        plt.fill_between(lambda_range, np.array(avg_wait_times) - np.array(conf_intervals),
                     np.array(avg_wait_times) + np.array(conf_intervals), alpha=0.2)

    # fig = plt.figure()
    plt.xlabel('Lambda (Poisson Arrival Rate)')
    plt.ylabel('Average Waiting Time')
    plt.title('M/M/1 Queue Simulation with 95% Confidence Intervals with 1000 round')
    plt.legend()
    plt.show()
    # fig.savefig("round " + num_simulations + ".png" ,dpi=500)



mm1_queue_plot()
arrival, wait, service_timne, leave = mm1_queue(lambda_possion= 1, customers = 10000, mu = 1)

print(average_wait_cal(wait))
cal_confident_interval(wait)
