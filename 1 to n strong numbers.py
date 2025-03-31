i=100
ams=[]
while i<50000:
    
    su=0
    
    
    bkp=i
    
    while bkp>0:
        t=bkp%10
        f=1
        while t>0:
            f=f*t
            
            t-=1
        su+=f
        
        bkp//=10
    if su==i:
            
        ams.append(su)
        
    i+=1
for i in ams:
    print(i)
    
