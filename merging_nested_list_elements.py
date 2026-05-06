x = [[1, 2], [3, 4], 5, [6, 7], 8]         #output = [1, 2, 3, 4, 5, 6, 7, 8]

# Method 1: Using list comprehension and isinstance() function

print([j for i in x for j in (i if isinstance(i,list) else[i])])


# method 2 : using recursive for loop

def merge_nested_list(lst,result=None):

    for item in lst:
        if isinstance(item, list):
            merge_nested_list(item, result)
        else:
            result.append(item)
        
    return result

print(merge_nested_list(x, []))