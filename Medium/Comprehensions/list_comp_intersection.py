# input
# x = [1, 2, 3, 4]
# y = [3, 4, 5, 6]

# expceted output 
# [3,4]

x = [1, 2, 3, 4]
y = [3, 4, 5, 6]

print([
   i for i in x if i in y
])