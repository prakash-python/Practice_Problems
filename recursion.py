def display(n):
    if n==1:
        return 1
    print(n)
    display(n-1)
    print(n)
res=display(5)

    
