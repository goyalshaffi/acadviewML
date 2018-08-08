t=(1,2,3,4)
#print(len(t))
l=[6,7,8]
#print(tuple(l))
#print(list(t))


print(t)
del t
#print(t)#print fun in del is used before del as error get as nt defined


#set

a=set ((1,2,3))
b=set ([3,4,5])
#print(a&b)#intersection
#print(a|b)#union
a.add("apple")
#print(a)
a.update(["a","b","c"])
print(a)
print(list(a))
#a.sort()
#print(a)
#a.pop()
#print(a)
#a.remove(2)
#a.discard(5)
#print(a)



r=([1,2,3,4,5])
w=([3,4,5])
print(r>=w)
print(r<=w)

#dictionary
d={'name':'anam',
   'age': 12}
print(d)
print(d['name'])
d['name']='roi'
print(d)


#functions of dictionary

#del d['name']
#print(d)

#d.clear()
#print(d)

del d
print(d)
