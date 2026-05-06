# input x = [1, 2, 3, 4, 5]         expected output [1, 8, 27, 64, 125]
x = [1, 2, 3, 4, 5]
print(list(map(lambda i: i **3 , x)))