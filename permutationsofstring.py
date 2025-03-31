'''def permutationsofstring(st,i=0):
    if i==len(st):
        print(''.join(st))
    for j in range(i,len(st)):
        words = [c for c in st]
        words[i],words[j] = words[j],words[i]
        permutationsofstring(words,i+1)
st=input('Enter a string to get permutations of that string:')
permutationsofstring(st)'''
'''def gameOfPiles(piles, k):
    xor_sum = 0
    for pile in piles:
        if pile < k:
            xor_sum ^= pile
        else:
            xor_sum ^= pile % (k + 1)
    
    if xor_sum == 0:
        return f"Alex wins the game of {len(piles)} pile(s)."
    else:
        return f"Sam wins the game of {len(piles)} pile(s)."'''


'''def getMaxOccurrences(components, minLength, maxLength, maxUnique):
    max_occurrences = 0
    freq_map = {}
    
    for length in range(minLength, maxLength + 1):
        for i in range(len(components) - length + 1):
            substring = components[i:i + length]
            unique_chars = len(set(substring))
            
            if unique_chars <= maxUnique:
                freq_map[substring] = freq_map.get(substring, 0) + 1
                max_occurrences = max(max_occurrences, freq_map[substring])
    
    return max_occurrences'''




'''def countSignals(frequencies, filterRanges):
    
    overlap = [filterRanges[0][0], filterRanges[0][1]]
    for filterRange in filterRanges[1:]:
        overlap[0] = max(overlap[0], filterRange[0])
        overlap[1] = min(overlap[1], filterRange[1])
    
    
    count = 0
    for frequency in frequencies:
        if overlap[0] <= frequency <= overlap[1]:
            count += 1
    
    return count'''



SELECT 
    e.dt, 
    e.title, 
    u.full_name, 
    u.email_address
FROM 
    events e
JOIN 
    users u ON e.user_id = u.id
WHERE 
    u.on_vacation = FALSE
ORDER BY 
    e.dt ASC
LIMIT 5;








































 

























