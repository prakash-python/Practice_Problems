n=int(input('enter a number:'))
x=[]
cnt=0
for i in range(2,10**6):
    is_prime=True
    for d in range(2,(i//2)+1):
        if i%d==0:
            is_prime=False
            break
    if is_prime:
           
        cnt+=1
        if cnt==n:
            print(i)
            break

    
        
    
    
