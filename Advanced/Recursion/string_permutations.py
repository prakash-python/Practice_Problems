# String permutations using recursion

def get_permutations(s, i=0):
    if i == len(s):
        print(''.join(s))
    
    for j in range(i, len(s)):
        words = [c for c in s]
        words[i], words[j] = words[j], words[i]
        get_permutations(words, i + 1)

if __name__ == "__main__":
    st = input("Enter a string to get permutations: ")
    get_permutations(list(st))
