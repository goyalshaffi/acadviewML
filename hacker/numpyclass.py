import numpy as np

a=np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)
'''

a=np.zeros((2,2))
print(a)
b=np.ones((1,2))
print(b)
c=np.full((2,2),7)
print(c)
d=np.eye(2)
print(d)
e=np.random.random((2,2))
print(e)


a=np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)#bytes of number

q=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(q)
b=np.array([0,2,0,1])
print(q[np.arange(4),b])
q[np.arange(4),b]+=10
print(q)


a=np.array([[1,2],[3,4],[5,6]])
bool_idx=(a==2)
print(bool_idx)

x=np.array([1,2])
print(x.dtype)

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
v=np.array([9,10])
w=np.array([11,12])
print(v.dot(w))
print(np.dot(v,w))

x=np.array([[1,2],[3,4]])
print(np.sum(x))
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))
print(x.T)
'''