# input x = [1, 2, 3, 4, 5, 6]        expected output [2,4,6]
from functools import reduce

x = [1, 2, 3, 4, 5, 6]
print(list(reduce(
    lambda acc, i: acc + [i**2] , x, []
)))