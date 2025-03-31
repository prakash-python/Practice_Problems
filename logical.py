y,*x = map(int,input().split())
x.sort()
cnt=0
while True:
    if x[0]==x[1]==x[2]:
        print(cnt)
        break
    x[0]+=1
    x[1]+=1
    x[2]-=1
    cnt+=1
    if x[2]<0:
        cnt=-1
        print(cnt)
        break
    
