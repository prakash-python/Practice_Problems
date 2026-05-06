# input x = [10, 20, 30, 40, 50]       expected output 50
from functools import reduce
x = [10, 20, 30, 40, 50]
print(reduce(
    lambda max_v, i: max(max_v,i), x, x[0]
))