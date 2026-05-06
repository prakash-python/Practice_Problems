'''prime=[]
def isprime(n):
    if n==1:
        return prime
    else:
        d=2
        for i in range(d,(n//2)+1):
            if n%i==0:
                return isprime(n-1)
    prime.append(n)
    return isprime(n-1)
def main(n):
    if n>=2:
        res=isprime(n)
        return res
    else:
        return f'There is no primes less than {n}'
n=int(input('Enter a number to find primes upto that number:'))
result=main(n)
if type(result)==list:
    print(result[::-1])
else:
    print(result)'''
s='this is prakash'
x=s.split()
for i in x:
    print(i[0])
