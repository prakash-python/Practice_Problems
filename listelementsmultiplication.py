x = [1, 2, 3, 4, 5]
y=[]

for i in range(len(x)):
    product = 1
    for j in range(len(x)):
        if i != j:
            product *= x[j]
    y.append(product)
    
print("List after multiplication:", y)

        
