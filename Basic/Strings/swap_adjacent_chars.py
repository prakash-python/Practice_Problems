input_num = int(input("Enter a number to sort every two numbers : "))
input_num = str(input_num)
output_str = ""
for i in range(0,len(input_num),2):
    
    if i+1 < len(input_num):
        output_str += input_num[i+1]+input_num[i]
    else:
        output_str += input_num[i]
print(output_str)