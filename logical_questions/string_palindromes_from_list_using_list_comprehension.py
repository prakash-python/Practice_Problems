#  input x = ['madam', 'apple', 'level', 'python']             expected output ['madam', 'level']

x = ['madam', 'apple', 'level', 'python']
print([i for i in x if i == i[::-1]])