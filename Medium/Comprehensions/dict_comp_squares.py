# input x = [1, 2, 3, 4, 5]   expected output {
#                                                 1: 1,
#                                                 2: 4,
#                                                 3: 9,
#                                                 4: 16,
#                                                 5: 25
#                                             }

x = [1, 2, 3, 4, 5]
print({i: i**2 for i in x})