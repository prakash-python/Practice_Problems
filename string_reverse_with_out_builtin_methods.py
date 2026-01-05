def reverse_string(s: str) -> str:
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Example usage:
input_string = input("Enter a string: ")
result = reverse_string(input_string)
print("Reversed string:", result)