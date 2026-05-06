def print_pattern(n):
    start_odd, start_even = 1, 2  # Initial values for odd/even rows
    mid = n // 2  # Midpoint to adjust spacing
    v=2
    for i in range(1, n + 1):
        # Adjust spacing: more for the first half, less for the second half
        
        '''spaces = (n - i) * 3+i if i <= mid else (((mid - (i - mid)) * 3)+v)
        print('(((mid - (i - mid)) * 3)+v)=',(((mid - (i - mid)) * 3)+v))
        print('v ',v)
        print('i=',i)
        print(spaces)
        print(" " * spaces, end="")  '''
        if i<=mid:
            print(' '*((n-i)*3+i),end='')
        else:
            
            print(' '*((mid-(i-mid))*3+v),end='')
            v-=1

        # Determine starting number (odd for odd rows, even for even rows)
        print('start_even=',start_even)
        print('start_odd=',start_odd)
        num = start_odd if i % 2 == 1 else start_even

        # Print numbers in the row
        for _ in range(i):
            print(num, end=" ")
            num += 2  

        print()  # Move to the next line
        
        # Update the starting values for the next row
        if i % 2 == 1:
            start_odd = num  
        else:
            start_even = num  

# Call the function
n = 6
print_pattern(n)
'''1 
              2 4 
            3 5 7 
        6 8 10 12 
     9 11 13 15 17 
  14 16 18 20 22 24'''
  
