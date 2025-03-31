i=1
while i<=10:
    d=2
    while d<=(i//2)+1:
        if i%d==0:
            break
        
        d+=1
    print(i)
    i+=1
