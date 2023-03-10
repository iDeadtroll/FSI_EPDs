from functools import reduce


l = [1, 2, 3]
l2 = reduce(lambda x, y: x + y, map(lambda x: x**2))