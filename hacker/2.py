l1=[]
l3=[]
l5=[]
l2=input("enter value")
l4=input("enter value")
l1.extend(l2)
l3.extend(l4)
print(l1)
print(l3)
for i in range(0,3):
    if(l1[i]>l3[i]):
        print('1')
    elif(l1[i]==l3[i]):
        pass
    else:
        print('0')


