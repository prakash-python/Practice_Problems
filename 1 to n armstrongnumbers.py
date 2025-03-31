n=int(input('Enter a number'))
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
    
    if s==i :
        
        print('sum after if ',s)
    i+=1
        
