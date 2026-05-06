# input x = [1, 2, 3, 4, 5, 6]             expected output = [2,4,6]
x = [1, 2, 3, 4, 5, 6]
output = list(filter(lambda i : i%2 == 0, x ))
print(output)

