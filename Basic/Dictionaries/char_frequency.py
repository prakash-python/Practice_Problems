# input s = "hello world"         expected output {
#                                                     'h': 1,
#                                                     'e': 1,
#                                                     'l': 3,
#                                                     ...
#                                                 }

s = "hello world"
d = {}
for i in s:
    if i == ' ':
        pass
    else:
        
        d[i] = d.get(i,0) + 1

print(d)