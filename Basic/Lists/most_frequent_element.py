x=[1,2,3,2,2,2,2,3,1,4,1,2,1]
d={}
cnt=1
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=cnt


for i in d:
    first=d[i]
    if d[i]>first:
        first=d[i]
print(i)
