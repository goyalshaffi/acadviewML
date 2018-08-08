num=int(input("enter number"))
if num%2==0:
    if num%3==0:
        print("divisible by 2 and3")
    else:
        print("divisible by 2 not by 3")
else:
    if num%3==0:
        print("divisible by 3 nit divisible by 2")
    else:
        print("not divisible by 2 not by 3")