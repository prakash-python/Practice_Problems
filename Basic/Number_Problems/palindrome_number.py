a=121

while a>0:
    print(a)
    t=a%10
    print(t)
    
    a=a//10
    print(a)
print(t)
if t==a:
    print('pallendrome')
else:
    print('not pallendrome')
