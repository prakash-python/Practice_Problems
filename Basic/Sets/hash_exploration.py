'''n = int(input())  # Read the first input (which is 2)
t = tuple(map(int, input().split()))  # Read the next line, split it into integers, and convert to tuple
print(hash(t))  # Print the hash of the tuple'''
# Adding elements and printing their hash values
names = set()

for name in ["Alice", "Bob", "Alice"]:
    print(f"Adding {name}, hash: {hash(name)}")
    names.add(name)
for num in [10,20,30,30,20,40]:
    names.add(num)
    print(hash(num))

print("Final set:", names)
