x=[1,2,3,4,5]

z=[]
for i in x:
    y=[]
    for j in range(i+1,len(x)):
        if i+x[j]==6:
            y.append(i)
            y.append(x[j])
            z.append(y)
print(len(z))
            
