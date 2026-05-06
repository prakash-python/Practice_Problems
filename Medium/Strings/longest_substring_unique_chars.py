"Here we are not going to consider sequence of characters we are just getting longest string with unique values"
st = "abcaefghbxyz"
max_unique_str = ""
for i in range(len(st)):

    if st[i] not in max_unique_str:
        max_unique_str += st[i]
    else:
        max_unique_str = max_unique_str[max_unique_str.index(st[i])+1:] + st[i]
        
    

print(max_unique_str)
print(len(max_unique_str))