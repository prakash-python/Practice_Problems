from collections import deque
my_queue = deque([9, 2, 3])
my_queue.append(4)  # Add to the right end
my_queue.appendleft(3)  # Add to the left end
my_queue.pop()  # Remove from the right end
my_queue.popleft()  # Remove from the left end
print(my_queue)
