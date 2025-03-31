'''def longestsubsequent(x):
    lst_set=set(x)
    lon_seq=[]
    for i in range(len(lst_set)):
        if i-1 not in lst_set:
            cur_num=i
            cur_seq=[]
            while cur_num in lst_set:
                cur_seq.append(cur_num)
                cur_num+=1
                
            if len(cur_seq)>len(lon_seq):
                lon_seq=cur_seq
                
    return lon_seq
lls=[1,100,200,400,300,3,2]
res=longestsubsequent(lls)
print((res))'''


'''lls = [1,1, 106, 102, 103, 3,101,104, 2,4,201,202]
res = set(lls)
print(res)
lon=[]
for i in sorted(res):
    
    
    if i-1 not in res:
        cur=i
        cu=[]
        while cur in res:
            cu.append(cur)
            cur+=1
        
        if len(cu) > len(lon) or (len(cu) == len(lon) and cu > lon):
            lon=cu

print(lon)'''


'''x=[1,2,3,4,5]
y=[101,102,103,104,105,106]
if (x>y or len(x)>=len(y)):
    print(x)
else:
    print(y)'''






























