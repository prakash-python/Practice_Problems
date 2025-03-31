'''x=[1,2,3]
x.append(x)
print(x)'''
'''x=[10,0,1,15]
y=[9,8,16,3]
z=(x+y)
for i in range(len(z)):
    for j in range(i+1):
        if z[i]<z[j]:
            z[i],z[j]=z[j],z[i]
print(z)'''
'''n=3
k=1
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    
    for j in range(1,i+1):
        print(k,end=' ')
        
    print()
    k+=1'''
n=5
m=(n//2)+1

i=1
while i<=n:
    print(' '*(m-i),end=' ')
    if i<=m:
        print(i,end=' ')
    print()
    i+=1
    
