def found_consonents_surrounded_by_vowels(input_str):
    if len(input_str) == 0:
        return "Empty Strings Are Not Allowed"
    if input_str == " ":
        return "Empty Spaces Are Not Allowed"
    
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    do_process = False
    for i in input_str:
        if i not in vowels:
            do_process = True
            break
    while do_process:
        tmp_output_str = ''
        output_str = ''
        co_st = 0
        vo_st = 0
        while vo_st < len(input_str):
            if input_str[vo_st] not in vowels:
                co_st = vo_st
                while co_st <= vo_st < len(input_str):
                    if input_str[co_st] in vowels:
                        output_str += tmp_output_str
                        tmp_output_str = ''
                        vo_st = co_st
                        break
                    else:
                        tmp_output_str += input_str[co_st]
                    co_st += 1
                    vo_st += 1
            vo_st += 1
        return output_str
    else:
        return "Ther is no Consonent in the given String"
input_str = input('Enter a string to found consonents surrounded by vowels : ')
if __name__ == '__main__':
    res = found_consonents_surrounded_by_vowels(input_str)

print(res)
