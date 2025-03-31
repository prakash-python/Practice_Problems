x=[5,3,8,2,1]

''' ************************selection sort
for i in range(len(x)):
    min_idx=i
    for j in range(i+1,len(x)):
        
        if x[j]<x[min_idx]:
            min_idx=j
    x[i],x[min_idx]=x[min_idx],x[i]
print(x)'''

''' ******************************** insertion sort
for i in range(1,len(x)):
    in_v = x[i]
    for j in range(i,-1,-1):
        
        if x[j-1]>in_v:
            x[j]=x[j-1]
            
        else:
            x[j]=in_v
            
            break
    x[j]=in_v
print(x)'''

'''******************************* Bubble sort

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)'''



























        
