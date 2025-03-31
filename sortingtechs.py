x=[5,3,8,2,1]

''' ************************selection sort
for i in range(len(x)):
    min_v=i
    for j in range(i+1,len(x)):
        
        if x[j]<x[min_v]:
            min_v=j
    x[i],x[min_v]=x[min_v],x[i]
print(x)'''

''' ******************************** insertion sort
for i in range(1,len(x)):
    in_v = x[i]
    for j in range(i,-1,-1):
        
        if x[j-1]>in_v:
            x[j]=x[j-1]
            
        else:
            x[j]=in_v
            
            break
    x[j]=in_v
print(x)'''

''' ******************************* Bubble sort

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)'''


#******************************* Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    
    middle = [x for x in arr if x == pivot]
    
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


numbers = [5, 3, 8, 10, 9]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 5, 8]




















        
