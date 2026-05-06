s='''we are python programing'''
cnt = 1
word = ''
for i in range(len(s)):
    
    if s[i]!=' ':
        word+=s[i]
        for j in range(i+1,len(s)):
            tmp = ''
            k=i+1
            while k<=len(s) and s[j]!=' ':
                tmp+=s[j]
                k+=1
            if s[i]==s[j]:
                cnt+=1
print(word,cnt)
