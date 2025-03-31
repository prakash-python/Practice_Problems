

x=[]
def smallest_prime_factor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def divisor_queries(N, Q, a, queries):
    
    for query in queries:
        if query[0] == 1:
            left, right = query[1], query[2]
            for i in range(left-1, right):
                factor = smallest_prime_factor(a[i])
                a[i] //= factor
        elif query[0] == 2:
            left, right = query[1], query[2]
            [(sum(a[left-1:right]))]
        else:
            index, value = query[1], query[2]
            a[index-1] = value
        return []

N, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]
rea=divisor_queries(N, Q,a,queries)
print(rea)

