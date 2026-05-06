# input s = "python django api"     output = "api django python"
s = "python django api"
words = s.split()
words = words[::-1]
output = " ".join(words)
print(output)

# second version 
print(" ".join(s.split()[::-1]))