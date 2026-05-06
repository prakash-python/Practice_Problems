x = 'aaabbcddd'      # expected output = a3b2c1d3
res = ''
count = 1
for i in range(1,len(x)):
    if x[i-1] == x[i]:
        count += 1

    else:
        res += x[i-1] + str(count)

        count = 1
res += x[-1] + str(count)

print(res)