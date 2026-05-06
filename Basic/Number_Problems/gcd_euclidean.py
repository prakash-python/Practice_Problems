n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1

while v>0:
    v=big%small
    if v==0:
        print(small)
        break
    big=small
    small=v

