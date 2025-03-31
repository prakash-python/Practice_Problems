n=int(input('Enter a number to print the pattern:'))
even=2
odd=1
mid=n//2
for i in range(1,n+1):
    
    if i<=mid:
        print(' '*((n-i)*3+i),end='')
    else:
        
        print(' '*(((mid-(i-mid))*3+(n-i))),end='')
        
    if i%2==1:
        num=odd
    else:
        num=even
    for j in range(i):
        print(num,end=' ')
        num+=2
    
    print()
    if i%2==1:
        odd=num
    else:
        even=num
