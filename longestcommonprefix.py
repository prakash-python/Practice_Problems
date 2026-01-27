def logpre(words):
    
    if not words:
        return ''
    lon_prefix=""
    
    for i in words:
        for j in range(len(i)):
            if j<len(lon_prefix):
                if lon_prefix[j]!=i[j]:
                    lon_prefix=lon_prefix[:j]
                    break
            else:
                lon_prefix+=i[j]
    return lon_prefix
words=['flower','flow','flight']
res=logpre(words)
print(res)
        
