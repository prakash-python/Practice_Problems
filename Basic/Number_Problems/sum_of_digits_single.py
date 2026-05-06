n=12345


while True:
    s=0
    while n>0:
        d=n%10
        
        s+=d
        n//=10
    
    if s>=10:
        n=s
    else:
        print(s)
        break
