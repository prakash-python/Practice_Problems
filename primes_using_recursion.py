def prime_check_using_recursion(n, d=2):
    
    if n < 2:
        return False
    if n == d:
        
        return True
    if n % d != 0:
        
        return prime_check_using_recursion(n, d + 1)

    return False

def primes_given__range_using_recursion(start,end):
    primes = []
    if start > end:
        return []
    else:
        if start == end and prime_check_using_recursion(start):
            return [start], 'prime number in the range'
        elif start < end:
            if prime_check_using_recursion(start):
                primes.append(start)
                
            return primes + primes_given__range_using_recursion(start + 1, end)
        else:
            return []
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
res = primes_given__range_using_recursion(start=start, end=end)
if type(res) is list:
    for i in range(len(res)):
        if i != len(res) - 1:
            print(res[i])
        else:
            print(res[i],' '*1,end = '')
            print('Are The Prime Numbers In The Range')

    
        
