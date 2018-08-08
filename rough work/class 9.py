'''

class Complex():
    def __init__(self):# self is perdefined keyword
        print("hello")
c=Complex()



class Complex():
    def __init__(self,real,imag):#taking two parameters real and imag
        self.r=real
        self.i=imag
c=Complex(3,4)
print(c.i)
print(c.r)

'''

class Apollo():
    destination="moon" #class variable
    def __init__(self):
        print("ready to launch")#or we can use pass

    def flying(self):
        print("spaceship is flyoing")
    def getdestination (self):
        print("the destinstion is"+self.destination)
a=Apollo()
a.flying()
a.getdestination()
b=Apollo()
b.destination="mars"
b.getdestination()




