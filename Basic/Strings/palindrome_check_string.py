# Check if a string is a palindrome

str_ = input("Enter a string: ")
reversed_str = ""

for char in str_:
    reversed_str = char + reversed_str

if str_ == reversed_str:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
