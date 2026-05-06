s = list("abc")  # Convert string to list for swapping
n = len(s)

# Stack to simulate recursion manually
stack = [(0, s[:])]  # Store (left index, current string state)
print(stack)

while stack:
    print('stack in while loop=',stack)
    left, current_s = stack.pop()
    print('left=',left)
    print('current_stack=',current_s)
    if left == n - 1:
        s=''
        print(s.join(current_s))# Print when one permutation is complete
        print('s=',s)
    else:
        for i in range(n - 1, left - 1, -1):  # Iterate in reverse to maintain order
            current_s[left], current_s[i] = current_s[i], current_s[left]  # Swap
            stack.append((left + 1, current_s[:]))  # Push new state to stack
            current_s[left], current_s[i] = current_s[i], current_s[left]  # Backtrack
