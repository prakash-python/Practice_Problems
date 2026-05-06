
num=input('Enter a number')

dn=0
i=0
while i<len(num):
    bi=int(num[i])
    dn+=bi*(2**(len(num)-i-1))
    i+=1
print(dn)
    
