import numpy as np
import random

def simulate_mm1_queue(lambda_arrival, mu_service, simulation_time, num_simulations):
    server_utilization = 0
    waiting_time_sum = 0
    waiting_time_list = []   # 這也都都怪怪的
    count_service = 0

    for _ in range(num_simulations):
        time = 0
        queue = []
        server_busy = False
        next_arrival = -np.log(1 - random.random()) / lambda_arrival

        while time < simulation_time:
            if next_arrival < mu_service and not server_busy:
                # Process the arrival
                server_busy = True
                service_time = -np.log(1 - random.random()) / mu_service
                server_utilization += service_time
                waiting_time = 0
            elif next_arrival <= mu_service and not server_busy:
                # Process the arrival, and there's an idle server
                server_busy = True
                service_time = -np.log(1 - random.random()) / next_arrival
                waiting_time = 0
            else:
                # Customer goes into the queue
                queue.append(time)
                waiting_time = 0

            if server_busy:
                # Server processing
                service_time -= next_arrival
                if service_time <= 0:
                    server_busy = False
                    next_arrival = -np.log(1 - random.random()) / lambda_arrival
                    if queue:
                        # Process the next customer from the queue
                        next_customer = queue.pop(0)
                        waiting_time = time - next_customer
                        server_busy = True
                        service_time = -np.log(1 - random.random()) / mu_service

            waiting_time_sum += waiting_time
            waiting_time_list.append(waiting_time)

            time += next_arrival
            count_service += 1

    server_utilization /= simulation_time             # 須改
    expected_waiting_time = waiting_time_sum / count_service

    return server_utilization, expected_waiting_time, waiting_time_list

# Example usage:
lambda_arrival = 5.0  # Arrival rate (customers per time unit)
mu_service = 6.0     # Service rate (customers per time unit)
simulation_time = 1000  # Total simulation time
num_simulations = 1000  # Number of simulation runs

utilization, expected_waiting_time, waiting_time_list = simulate_mm1_queue(lambda_arrival, mu_service, simulation_time, num_simulations)

print(f"Server Utilization: {utilization}")
print(f"Expected Waiting Time: {expected_waiting_time}")
print(waiting_time_list)