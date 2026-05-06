# input x = 'python'    expected output = 'nohtyp'
s = 'python'
output = ''
for i in range(len(s),0,-1):
    output += s[i-1]

print(output)