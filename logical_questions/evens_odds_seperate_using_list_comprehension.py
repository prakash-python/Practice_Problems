# input x = [1, 2, 3, 4, 5, 6]   expected output {
#                                                     'even': [2, 4, 6],
#                                                     'odd': [1, 3, 5]
#                                                 }

x = [1, 2, 3, 4, 5, 6]
d = {
    'even':[i for i in x if i %2 == 0],
    'odd':[i for i in x if i%2 != 0]
}
print(d)