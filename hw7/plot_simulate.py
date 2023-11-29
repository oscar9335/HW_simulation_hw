import numpy as np
import matplotlib.pyplot as plt
import csv
import ast
from decimal import Decimal

def read_csv_file(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list

def plot_IQ_Luck(path,indicator):

    the_bin = 0
    if indicator == 0:
        the_bin = 120
    elif indicator == 2:
        the_bin = 80
        

    # Example usage:
    mostleast_wealth_people = path
    mostleast_wealth_people_csv_data = read_csv_file(mostleast_wealth_people)

    # print(most_wealth_people_csv_data)

    most_wealth_people_list = []

    for item in mostleast_wealth_people_csv_data:
        string_representation = item[0]
        most_wealth_people_list.append(ast.literal_eval(string_representation))

    iq_values = [item[indicator] for item in most_wealth_people_list if isinstance(item, list)]


    # Plotting histogram
    plt.hist(iq_values, bins=the_bin, edgecolor='black',alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Values')

    # Calculate mean and standard deviation
    mean_iq = np.mean(iq_values)
    std_iq = np.std(iq_values)

    # Plot lines for one standard deviation above and below the mean
    plt.axvline(mean_iq, color='red', linestyle='dashed', linewidth=2, label='Mean')
    plt.axvline(mean_iq + std_iq, color='yellow', linestyle='dashed', linewidth=2, label='+1 Std Dev')
    plt.axvline(mean_iq - std_iq, color='yellow', linestyle='dashed', linewidth=2, label='-1 Std Dev')



    # Mark the mean and one standard deviation on the plot with adjusted vertical positions and more obvious text
    plt.annotate(f'Mean: {mean_iq:.2f}', xy=(mean_iq, 0), xytext=(mean_iq, 200),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, fontweight='bold', color='red')
    plt.annotate(f'+1 Std Dev: {mean_iq + std_iq:.2f}', xy=(mean_iq + std_iq, 0), xytext=(mean_iq + std_iq, 250),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, fontweight='bold', color='black')
    plt.annotate(f'-1 Std Dev: {mean_iq - std_iq:.2f}', xy=(mean_iq - std_iq, 0), xytext=(mean_iq - std_iq, 300),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, fontweight='bold', color='black')

    # Show legend
    plt.legend()

    # Display the plot
    plt.show()

def plot_start_wealth(path):

    # Example usage:
    mostleast_wealth_people = path
    mostleast_wealth_people_csv_data = read_csv_file(mostleast_wealth_people)

    # print(most_wealth_people_csv_data)

    most_wealth_people_list = []

    for item in mostleast_wealth_people_csv_data:
        string_representation = item[1]
        most_wealth_people_list.append(ast.literal_eval(string_representation))

    # iq_values = [item[indicator] for item in most_wealth_people_list if isinstance(item, list)]


    # Plotting histogram
    plt.hist(most_wealth_people_list, bins=50, edgecolor='black',alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Values')

    # Calculate mean and standard deviation
    mean_iq = np.mean(most_wealth_people_list)
    std_iq = np.std(most_wealth_people_list)

    # Plot lines for one standard deviation above and below the mean
    plt.axvline(mean_iq, color='red', linestyle='dashed', linewidth=2, label='Mean')
    plt.axvline(mean_iq + std_iq, color='yellow', linestyle='dashed', linewidth=2, label='+1 Std Dev')
    plt.axvline(mean_iq - std_iq, color='yellow', linestyle='dashed', linewidth=2, label='-1 Std Dev')



    # Mark the mean and one standard deviation on the plot with adjusted vertical positions and more obvious text
    plt.annotate(f'Mean: {mean_iq:.2f}', xy=(mean_iq, 0), xytext=(mean_iq, 200),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, fontweight='bold', color='red')
    plt.annotate(f'+1 Std Dev: {mean_iq + std_iq:.2f}', xy=(mean_iq + std_iq, 0), xytext=(mean_iq + std_iq, 400),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, fontweight='bold', color='black')
    plt.annotate(f'-1 Std Dev: {mean_iq - std_iq:.2f}', xy=(mean_iq - std_iq, 0), xytext=(mean_iq - std_iq, 600),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, fontweight='bold', color='black')

    # Show legend
    plt.legend()

    # Display the plot
    plt.show()

def a_person_life_most(path):
     # Example usage:
    aaa = path
    aaa_csv_data = read_csv_file(aaa)


    new_list = []

    for item in aaa_csv_data[0]:
        # Convert to float
        large_number_float = float(item)
        new_list.append(large_number_float)

    print(new_list)

    # Define the indices for plotting
    indices = [0] + list(range(9, len(new_list), 10)) + [len(new_list)-1]
    

    # Plot the list
    plt.plot(indices, [new_list[i] for i in indices], marker='o')

    plt.xlabel('a Event occur')
    plt.ylabel('Wealth')
    plt.scatter([0, len(new_list)-1], [new_list[0], new_list[-1]], color='red')
    # plt.yticks([new_list[0], new_list[-1]])
    # Set x-axis ticks to show the selected indices
    # plt.xticks(indices)
    plt.show()
    

    # print(aaa_csv_data[0])

def a_person_life_least(path):
     # Example usage:
    aaa = path
    aaa_csv_data = read_csv_file(aaa)

    integer_list = [int(value) for value in aaa_csv_data[0]]

    # Plot the list
    plt.plot(integer_list)
    plt.xlabel('a Event occur')
    plt.ylabel('Wealth')
    plt.scatter([0, len(integer_list)-1], [integer_list[0], integer_list[-1]], color='red')
    plt.yticks([integer_list[0], integer_list[-1]])
    plt.show()

def event_count(path):
    # Example usage:
    aaa = path
    a_csv_data = read_csv_file(aaa)

    count_F = 0
    count_D = 0
    count_B = 0
    count_A = 0
    count_S = 0

    for item in a_csv_data[0]:
        if item == 'F':
            count_F+=1
        elif item == 'D':
            count_D+=1
        elif item == 'B':
            count_B+=1
        elif item == 'A':
            count_A+=1
        elif item == 'S':
            count_S+=1

    print("F: "+ str(count_F) )
    print("D: "+ str(count_D) )
    print("B: "+ str(count_B) )
    print("A: "+ str(count_A) )
    print("S: "+ str(count_S) )
    

# a_person_life_most('csv_file_most_wealth_people_wealth_change.csv')
# a_person_life_least(' csv_file_least_wealth_people_wealth_change.csv')

# 最後財富最多事件數
print("最後財富最多事件數")
event_count('csv_file_most_wealth_people_event.csv')

# 最後財富最少事件
print("最後財富最少事件數")
event_count('csv_file_least_wealth_people_event.csv')

# # 最後財富最多的IQ分布
# plot_IQ_Luck('most_wealth_people.csv',0)
# # 最後財富最少的IQ分布
# plot_IQ_Luck('least_wealth_people.csv',0)
# # 最後財富最多的Luck分布
# plot_IQ_Luck('most_wealth_people.csv',2)
# # 最後財富最少的Luck分布
# plot_IQ_Luck('least_wealth_people.csv',2)
# # 最後財富最多的初始財富分布
# plot_start_wealth('most_wealth_people.csv')
# 最後財富最少的初始財富分布
# plot_start_wealth('least_wealth_people.csv')

