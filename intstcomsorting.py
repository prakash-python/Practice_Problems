x=[1,'pama',3,'pita',2]
strs=[i for i in x if type(i)==str]
dig=[i for i in x if type(i)==int]
output=[]

        
    
for i in range(len(strs)):
    smallest=i
    for j in range(i+1,len(strs)):
        if strs[j]<strs[smallest]:
            smallest=j
    strs[i],strs[smallest]=strs[smallest],strs[i]
for i in range(len(dig)):
    sma=i
    for j in range(i+1,len(dig)):
        if dig[j]<dig[sma]:
            sma=j
    dig[i],dig[sma]=dig[sma],dig[i]
    

output=dig+strs
print(output)
