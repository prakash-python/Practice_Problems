
# The function left_greater_values takes a list of numbers and returns a new list containing only 
# those elements that are greater than or equal to all the elements to their right in the original list.
    

def left_greater_values(x):
    is_all_le = True
    output = []
    for i in range(len(x)-1):

        for j in range(i+1,len(x)):

            if x[i] < x[j]:
                is_all_le = False
                break
            else:
                is_all_le = True
        if is_all_le:
            output.append(x[i])

    output.append(x[len(x)-1])
    return output

# Example usage:
input_list = list(map(int, input("Enter numbers separated by space: ").split()))  
result = left_greater_values(input_list)    
print(result)  # Output: [6]


