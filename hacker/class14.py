'''
#f=open("test.txt","r")
#print(f)
#print(f.read())

#print(f.readline())
#print(f.readline())

#print(f.readlines())

'''
f=open("test.txt","a")
#f.write("hello")
l=["A","B","C"]
#l=["A/n","B/n","C/n"]


#f.write(l)

f.writelines(l)




'''
with open("test.txt","r") as f:
  # print( f.read)
   #print(f.read(5))
   #print(f.tell())
  f.seek(0,2)
  print(f.tell())
  print(f.read())
'''


s=str(input("enter the string"))
f=open("test3.txt","r")
count=0
for word in f.read().split():
    if(s!=word in f.read().split()):
        count=0
    else:
        count=count+1
print(count)

# q 2
with open("test4.txt","w") as f:
    with open("test3.txt", "w") as f1:
            f1.write(f)
'''
