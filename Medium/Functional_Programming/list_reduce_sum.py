# input x = [1, 2, 3, 4, 5]           expected output 15

from functools import reduce

x = [1, 2, 3, 4, 5]
print(reduce(lambda output, i: output + i, x, 0))