# input x = ['apple', 'banana', 'apple', 'orange', 'banana']

# expected_output -->

# {
#     'apple': 2,
#     'banana': 2,
#     'orange': 1
# }

x = ['apple', 'banana', 'apple', 'orange', 'banana']
d = {}

# one way
for i in x:
    d[i] = x.count(i)

d1 = {}
# second version 
for i in x:
    d1[i] = d1.get(i,0) + 1

print(d)
print(d1)