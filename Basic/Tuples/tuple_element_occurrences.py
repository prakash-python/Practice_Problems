'''n=int(input('enter a number :'))

t=(1,2,3,4,2,5,6,2,7,8)
first=t.index(n)
for i in range(len(t),-1,-1):
    if t[i-1]==n:
        print('last in if',t.index(t[i])-1)
        break
idx=[]
for i in range(len(t)):
    if t[i]==n:
        idx.append(i)
print(idx[0],max(idx))
        
        
last=len(t)-1-t[::-1].index(n)
print(first,last)'''


''''x=[2,1,3,4,5,2,4,5]
print(x.remove(4))
z=[]
id_=0
n=int(input('enter a n '))
for i in range(len(x)-1):
    if x[i-1]==n:
        z.append(i)
        id_=z[0]
    print(z)
    
    x.remove(x[id_])
print(x)'''
x=[1,2,3,4,5,6,7,4,3,4]
N=int(input())
for i in x:
    if i==N:
        print(x[i])
        break
    x.remove(x[i])
    print(x)
else:
    print('not found')
