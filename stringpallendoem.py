str_='viv'
output=''
i=len(str)
while i>0:
    output+=str[i-1]
    i-=1
if output==str_:
    print('given string is pallendrome')
else:
    print('not a pallendrome')    
