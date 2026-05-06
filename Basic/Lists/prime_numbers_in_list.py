x=[1,2,3,4,5]
y=[]
for i in x:
    cnt=0
    for d in range(1,i+1):
        if i%d==0:
            cnt+=1
    if cnt==2:
        y.append(i)
print(y)
