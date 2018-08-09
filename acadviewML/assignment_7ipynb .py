# question1
#import numpy library

import numpy as np
a=np.random.random((10,1))
print(a.shape)     # printing shape of array
print(a)           # print array
b=np.mean(a)
print(b)           #mean of array

# question 2

c=np.random.random((20,1))
print(c.shape)
print(c)
d=np.var(c)  # to find out variation
print(d)
e=np.std(c)   #to find out standard deviation
print(e)


# question 3

A=np.random.random((10,20))
B=np.random.random((20,25))
f=np.matmul(A,B)     #to find the multipication af an array
print(f)
print(f.shape)       # shape of array after multipication of A and B array
G=np.sum(f)          # sum of elements of array G
print(G)


# question 4
from math import exp
H=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(H.shape)
print(H)


def f(x):
    return (1 / (1 + exp(-x)))


for i in range(1, 10):
    K=f(i)
    print(K)
    S=np.append(S,[K],axis=0)
    print(S)
