n=int(input('enter a number:'))
a=0
b=1
cnt=2
#print(a,b,end=' ')
while True:
    c=a+b
    cnt+=1
    if cnt==n:
        print(c)
        break
        
    a=b
    b=c
    
