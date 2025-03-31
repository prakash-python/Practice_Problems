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