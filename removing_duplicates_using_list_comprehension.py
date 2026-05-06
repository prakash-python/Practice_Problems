x = [1,2,2,3,4,4,5]        # output = [1,2,3,4,5]

print([j for i, j in enumerate(x) if j not in x[:i]])