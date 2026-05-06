# Triangle pattern printing

n = 5
m = (n // 2) + 1

i = 1
while i <= n:
    print(' ' * (m - i), end=' ')
    if i <= m:
        print(i, end=' ')
    print()
    i += 1
