def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    
    return merge(left,right)
def merge(left,right):
    print('left=',left)
    print('right=',right)
    sorte=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorte.append(left[i])
            i+=1
        else:
            sorte.append(right[j])
            j+=1
    sorte.extend(left[i:])
    sorte.extend(right[j:])
    return sorte
arr=[45,32,63,25,99,6]
res=mergesort(arr)
print(res)
        
