mylist=[] # create a empty list
print(mylist)

# Create a list of strings.
string_list = ["Hello", "Python", "World"]
print(string_list)

# Create a list of numbers.
number_list = [3, 4, 5, 6, 8, 10]
print(number_list)

# Create a list of boolean values.
boolean_list = [True, False, False, True]
print(boolean_list)

# Create a mixed list or list with heterogeneous data
mixed_list = [3, 4, "Python", True]
print(mixed_list)


names = ["Jeff", "Bill", "Steve", "Mohan"]
print(names[0]) # returns "Jeff"
print(names[1]) # returns "Bill"
print(names[2]) # returns "Steve"
print(names[3]) # returns "Mohan"
print(names[-3]) # returns "Bill"
# print(names[4]) # IndexError: list index out of range


# ===================== LIST Function ===================
# Create a string.
my_string = "Hello World"
# Create a list of characters from my_string.
character_list = list(my_string)
# Create a list of substrings from my_string.
substring_list = my_string.split()
# Print the results.
print(my_string)        # Output: "Hello World"
print(character_list)   # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(substring_list)   # Output: ['Hello', 'World']



# =========== Replacing or Updating elements in a list ===============
# Create a list.
my_list = [1, 2, 3, 4, 5]
print("before:",my_list)
# Modify an element in the list.
# Note that the first element in
# a list is at index 0.
my_list[2] = 7
my_list[4] = 10
# Print the result.
print("after:", my_list)  # output: [1, 2, 7, 4, 10]


my_mix_list = [1, "Hello Python", 7.98]
# Output: 'Hello Python'
print("before: ", my_mix_list[1])

# Output: 'Hello JavaScript'
# my_mix_list[1] = "Hello JavaScript"
my_mix_list[1] = 22
print("after: ", my_mix_list[1])
print(my_mix_list)


print('============= List Methods==============\n')

# Create a empty list
my_list = []

# Add a new element to the list
my_list.append(1) # [1]
my_list.append(2) # [1,2]
my_list.append(3) # [1,2,3]

other_nums = [4,5,6]

# Extend my_list with other_nums
my_list.extend(other_nums)

# Insert a new value at the index provided
my_list.insert(2, 33)
my_list.insert(4, 33)
print('BEFORE:: ', my_list)

# delete a value provided
my_list.remove(33)
# my_list.remove(100) # ValueError

print('AFTER:: ', my_list)

# ===== Sort list 
my_list.sort()
print(my_list)

unsorted_list = [3,2,55,22,56,88]
unsorted_list.sort(reverse=True)
print(unsorted_list)


# ==== List concat
list_1 = [1,2,3]
list_2 = [4,5,6]

new_list = list_1 + list_2

list_2.append(7)

print(list_2)
print('Concat Lists: ', new_list)

for value in new_list:
    # print(value * 2)
    pass 

print('LEN: ', len(new_list))

copy_list = list_1 + list_2

for index in range(len(new_list)):
    # print(new_list[index] + copy_list[index])
    pass
    
for index, value in enumerate(new_list):
    # print(f"Index: {index}, Value: {value}")
    pass 

# ===== Random Module =========
import random

values = []

for i in range(5):
    # values.append(random.randint(1, 100))
    pass

print(values)

# ========== Nested Lists =========
my_nested_list = [
   # 0, 1, 2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9],  # 2
    ['apple', 'banana', 'orange'] # 3
]

print(my_nested_list[0][2])
print(my_nested_list[2][1])
print(my_nested_list[3][2])

for outer in my_nested_list:
    for element in outer:
        print(element)
        
        
nums = [
    1, 2, 3, 
    [4, 5, 6, [7, 8, [9]]], 
    10
]

print(nums[3])
print(nums[3][3])
print(nums[3][3][2])



