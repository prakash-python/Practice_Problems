# Basic LCM of two numbers

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

larger = max(n1, n2)
while True:
    if larger % n1 == 0 and larger % n2 == 0:
        lcm = larger
        break
    larger += 1

print(f"The LCM of {n1} and {n2} is {lcm}")
