def logpre(words):

    if not words:
        return ''

    prefix = ''

    for i in range(len(words[0])):

        char = words[0][i]

        for word in words[1:]:

            if i >= len(word) or word[i] != char:
                return prefix

        prefix += char

    return prefix


words = ['flower', 'flow', 'flight']

res = logpre(words)

print(res)