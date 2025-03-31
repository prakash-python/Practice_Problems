x=['sita','rama','pava']
for i in range(len(x)):
    sm=i
    print('smallestoutofj=',sm)
    for j in range(i+1,len(x)):
        print('x[',j,']=',x[j])
        print('x[',sm,']=', x[sm])
        if x[j]>x[sm]:
            sm=j
            print('smallinif=',sm)
    x[j],x[sm]=x[sm],x[j]
print(x)
