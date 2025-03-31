def is_prime(num,divisior=None):
    if num<2:
        return False
    if divisior==None:
        divisior=num-1
    if divisior==1:
        return True
    if num%divisior==0:
        return False
    return is_prime(num,divisior-1)
def nth_prime(n,current=2,count=0):
    if n==count:
        return current-1
    if is_prime(current):
        return nth_prime(n,current+1,count+1)
    return nth_prime(n,current+1,count)

n=int(input('Enter a number :'))
res=nth_prime(n)
print('The',n,'prime number is ',res)
