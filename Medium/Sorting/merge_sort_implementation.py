def Merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = Merge_sort(arr[:mid])
    right = Merge_sort(arr[mid:])
    return Merge(left,right)

def Merge(left,right):
    sorted_array = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

arr = [23,34,54,6,3,99,45]
res = Merge_sort(arr)
print(res)

