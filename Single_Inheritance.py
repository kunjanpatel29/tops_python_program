"""
Inheritance : Creating New Class from an Existing Class is Called Inheritance.
The Object of one Class acquire the property of Object of another class is called Inheritance.

Single Inheritance : Creating New Class from an Existing Class is Called Single Inheritance.
Create Child Class Using Parent Class is also called Single Inheritance.

"""

class A:                        # Parent Class

    def getA(self,a):
        self.a = a
        
    def putA(self):
        print("A : ",self.a)

class B(A):                     # Child Class

    def getB(self,b):
        self.b = b

    def putB(self):
        print("B : ",self.b)

b1 = B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()
