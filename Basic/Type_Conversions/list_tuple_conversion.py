my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Convert list to tuple
print(my_tuple, type(my_tuple))  # Output: (1, 2, 3) <class 'tuple'>

new_list = list(my_tuple)  # Convert tuple back to list
print(new_list, type(new_list))  # Output: [1, 2, 3] <class 'list'>
