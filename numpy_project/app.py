import numpy as np

# python list
list_1 = [1,2,3,4,5]
print('LIST: ', list_1)
print(type(list_1))

# turn a list or dataset into a numpy array
my_array = np.array(list_1)

print('ARRAY: ', my_array)
print(type(my_array))
print(type(my_array[3]))

# ==========
my_darray = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
])

#             [row, col]
print(my_darray[0, 1])
print(my_darray[1, 2])

#         [row:row, col:col]
print(my_darray[:, 1:3])