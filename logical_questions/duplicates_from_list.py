# input x = [1, 2, 3, 2, 4, 5, 1]           expected output [1,2]
x = [1, 2, 3, 2, 4, 5, 1]
output = []
for i in x:
    if x.count(i) > 1 and i not in output:
        output.append(i)
print(output)

# second version 

print([val for idx,val in enumerate(x) if x.count(val) > 1 and val not in x[:idx]])

