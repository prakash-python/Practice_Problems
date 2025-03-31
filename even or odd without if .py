def is_prime(n,d=None):
    if n<2:
        return False
    if d==None:
        d=n-1
    if d==1:
        return True
    if n%d==0:
        return False
    return is_prime(n,d-1)
def nth_prime(num,current=2,cnt=0):
    if cnt==num:
        return current-1
    if is_prime(current):
        return nth_prime(num,current+1,cnt+1)
    return nth_prime(num,current+1,cnt)
n=int(input('Enter a number : '))
res=nth_prime(n)
print(res)
    
        
