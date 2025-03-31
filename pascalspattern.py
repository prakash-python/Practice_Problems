'''rows = int(input("Enter the number of rows for Pascal's Triangle: "))

row = 0
while row < rows:
    col = 0
    num = 1  
    spaces = " " * (rows - row - 1)  
    print(spaces, end="")  
    while col <= row:
        print(num, end=" ")  
        num = num * (row - col) // (col + 1)  
        col += 1
    print()  
    row += 1'''
'''n=int(input('Enter a number to print pascals triangle'))
for i in range(n):
    num=1
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()'''



n=int(input('Enter a number :'))
i=0
while i<n:
    num=1
    print(' '*(n-i-1),end='')
    j=0
    while j<i+1:
        print(num,end=' ')
        num=num*(i-j)//(j+1)
        j+=1
    
    print()
    i+=1
























