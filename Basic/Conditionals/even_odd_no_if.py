# Check if a number is even or odd without using an if condition

num = int(input("Enter a number: "))

# Using list indexing to avoid if-else
results = ["Even", "Odd"]
print(f"The number {num} is {results[num % 2]}")
