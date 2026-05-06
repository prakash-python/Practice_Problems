# x = ['python', 'django', 'api']  expected output ['PYTHON', 'DJANGO', 'API']
x = ['python', 'django', 'api']
output = list(map(lambda i : i.upper(), x))
print(output)