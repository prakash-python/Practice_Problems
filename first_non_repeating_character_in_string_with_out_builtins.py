from re import L


def first_non_repeating_char(s: str) -> str:
    if not s:
        return "Empty string will not be processed."
    
    if len(s) == 1:
        return s[0]
    

    
    if s.isnumeric():
        return "String with only numbers will not be processed."

    counts = {}

    for i in s:
        if i in counts:
            counts[i] += 1

        else:
            counts[i] = 1

    for i in counts:
        if counts[i] == 1:
            return i
        
input_str = input("Enter a string: ")
result = first_non_repeating_char(input_str)
if result:
    print(f"The first non-repeating character is: {result}")