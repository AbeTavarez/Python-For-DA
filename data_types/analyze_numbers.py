# Write a Python program that will generate 100 random integers and calculate the average of those integers and find out how many integers are above the average.

import random

# Todo 1 - Generate 100 random integers
random_num_list = []

for i in range(100):
    num = random.randint(1, 100)
    random_num_list.append(num)

print('LENGTH: ', len(random_num_list))
print('\nRANDOM NUM LIST: ', random_num_list)


# TODO 2 - Calculate the average of those integers
total_sum = 0

for num in random_num_list:
    total_sum += num

print("\nCALCULATED TOTAL: ", total_sum)

average = total_sum / len(random_num_list)
print("\nCALCULATED AVERAGE: ", average)


# TODO 3 - Find out how many integers are above the average
ints_above_average = 0

for num in random_num_list:
    if num > average:
        ints_above_average += 1

print('INTS ABOVE AVERAGE: ', ints_above_average)