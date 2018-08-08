'''
def solveMeFirst(a, b):
    res = a + b
    return(res)


# Hint: Type return a+b below


num1 = int(input())
num2 = int(input())
result = solveMeFirst(num1, num2)
print(result)

'''


for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k,end=" ")
    print(" ")
