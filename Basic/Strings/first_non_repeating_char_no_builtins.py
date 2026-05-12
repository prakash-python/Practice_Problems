
def first_non_repeating_char(s: str) -> str:
    
    counts = {}

    for i in s:
        if i == ' ':
            continue

        counts[i] = counts.get(i, 0) + 1

    for i in s:
        if i != ' ' and counts[i] == 1:
            return i

    return None
        
input_str = input("Enter a string: ")
result = first_non_repeating_char(input_str)
if result:
    print(f"The first non-repeating character is: {result}")