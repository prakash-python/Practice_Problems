n=int(input('Enter a number : '))
i=10
while i<=n:
    s=0
    bkp=i
    
    d_cnt=0
    while bkp>0:
        bkp//=10
        d_cnt+=1
    bkp=i
    
    while bkp>0:
        t=bkp%10
        s+=t**d_cnt
        bkp//=10
    

    i+=1

if s==n :
    print('The given number is an Armstrong Number')
else:
    print('The given number is not an Armstrong Number')
    
