input_str = input('Enter a string to get first non repeating character : ')
visited_values = ''
for i in input_str:
    if i not in visited_values:
        visited_values += i
    else:
        visited_values = visited_values.replace(i," ")
for i in visited_values:
    if i == " ":
        visited_values = visited_values.strip(i)

print(visited_values[0])