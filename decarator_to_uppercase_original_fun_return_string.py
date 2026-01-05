


def wrapperfunc(original_func):
    def inner(input_string):
        result = original_func(input_string)
        if result is None:
            return None
        if result == "":
            return ""
        if result.isspace():
            return " "
        if result.isnumeric():
            return result
        if result.isupper():
            return result
        return result.upper()
    return inner


@wrapperfunc
def original(input_string):
    if input_string is None:
        return None
    return input_string.lower()

# Example usage:
if __name__ == "__main__":
    print(original("hello world"))  # Output: "HELLO WORLD"
    print(original("12345"))        # Output: "12345"
    print(original("   "))          # Output: " "
    print(original(""))             # Output: ""
    print(original(None))           # Output: None
    print(original("ALREADY UPPER")) # Output: "ALREADY UPPER"

