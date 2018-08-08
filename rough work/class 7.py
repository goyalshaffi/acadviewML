'''
def fn():
    print("hello")#call by value
fn()


def fn(a):
    print(a)#call by reference
fn("hello world")


'''
#three types of parameters  required,keyword,default


def add(a,b=2):
    c=a+b
    d=a-b
    #print(c,d)
#add(b=2,a=7)


#add(a=2,b=3)


#add(2)

    return d,c
a,b=add(2,3)
print(str(a)+" "+str(b))

'''

n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
             sum=sum+i
    if(sum==n):
        return True
    else:
        return False
print(perfect(n))
for i in range(1,1001):
    if(perfect(i)==True):
        print(i)
'''









