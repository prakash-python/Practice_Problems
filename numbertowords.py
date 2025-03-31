'''# Function to convert numbers to words
def number_to_words(num):
    if num == 0:
        return "zero"

    # Define words for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Initialize result
    result = ""

    # Process hundreds
    if num >= 100:
        result += ones[num // 100] + " hundred"
        num %= 100
        if num != 0:
            result += " "

    # Process tens
    if 10 < num < 20:
        result += teens[num % 10]
    else:
        if num >= 10:
            result += tens[num // 10]
            num %= 10
            if num != 0:
                result += "-"
        if num > 0:
            result += ones[num]

    return result

# Input number
num = int(input("Enter a number (0-999): "))

# Convert to words
print(f"{num} in words is: {number_to_words(num)}")'''

num=int(input('enter a number between (0-999): '))
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if num< 0:
    print('Enter a valid number')
elif num==0:
    print('Zero')
else:
    if num>






















