st = input('Enter a string to get longest substring from the given string : ')
max_str = ""
cur_str = ""
equ_sub_strs = []
for i in range(len(st)):
    if ord(st[i]) == ord(st[i-1]) + 1:
        cur_str += st[i]
    else:
        cur_str = st[i]
    if len(cur_str) > len(max_str):
        max_str = cur_str
        equ_sub_strs = [cur_str]
    elif len(cur_str) == len(max_str) and cur_str not in equ_sub_strs:
        equ_sub_strs.append(cur_str)
print(equ_sub_strs)
print(max_str)