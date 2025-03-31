def StringChallenge(strArr):
    # Extract the decimal and binary strings
    decimal_number = int(strArr[0])  # Convert the decimal string to an integer
    binary_string = strArr[1]       # Get the binary string

    # Convert the decimal number to binary
    decimal_binary = bin(decimal_number)[2:]  # [2:] removes the '0b' prefix

    # Pad the binary strings to be of equal length
    max_length = max(len(decimal_binary), len(binary_string))
    decimal_binary = decimal_binary.zfill(max_length)
    binary_string = binary_string.zfill(max_length)

    # Compare the two binary strings and count differences
    differences = sum(1 for i in range(max_length) if decimal_binary[i] != binary_string[i])

    return differences

# Examples
print(StringChallenge(["5624", "0010111111001"]))  # Output: 2
print(StringChallenge(["44", "111111"]))          # Output: 3
