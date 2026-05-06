# input x = ['apple', 'banana', 'kiwi']     expected output   ['APPLE', 'BANANA', 'KIWI']

x = ['apple', 'banana', 'kiwi']
print([i.upper() for i in x if isinstance(i,str)])