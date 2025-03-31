def logpre(words):
    print('words at starting=',words)
    if not words:
        return ''
    prefix=words[0]
    print('prefix at intialisation=',prefix)
    for word in words[1:]:
        print('word in for loop=',word)
        while not word.startswith(prefix):
            prefix=prefix[::-1]
            print('prefix in side for and while loop=',prefix)
            if not prefix:
                return ''
    print('at last prefix=',prefix)
    return prefix
words=['flower','flow','flight']
res=logpre(words)
print(res)
        
