x=[1,2,3,2,2,2,2,3,1,4,1,2,1]
d={}

for i in x:
    d[i] = d.get(i,0) + 1

for i in d:
    first=d[i]
    if d[i]>first:
        first=d[i]
print(i)


