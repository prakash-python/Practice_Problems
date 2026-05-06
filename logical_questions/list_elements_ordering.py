# input x = [10,20,30,40]       expected_output = [20,30,40,10]

# first version

x = [10,20,30,40]
y = x[1:]
y.append(x[0])
print(y)

# second version 

y = x[1:] + x[:1]
print(y)
