a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
result = 0
for i in range(abs(b)):
    result += a
if b < 0:
    result = -result
print("Multiplication result:", result) 