"""
Hybrid Inheritance : The Combination of more than one type of inheritance is also called Hybrid Inheritance.
The consisting of multiple types of inheritance is called Hybrid Inheritance.

Father Have Three Sons(Child) and Grand Father Have a Son(Father)
"""

class A:                         # Parent Class
    
    def getA(self,a):
        self.a = a
    def putA(self):
        print("A : ",self.a)

class B(A):                      # Child Class1
    
    def getB(self,b):
        self.b = b
    def putB(self):
        print("B : ",self.b)
        
class C(A):                      # Child Class2

    def getC(self,c):
        self.c = c
    def putC(self):
        print("C : ",self.c)

class D(B,C):                    # Child Class3

    def getD(self,d):
        self.d = d
    def putD(self):
        print("D : ",self.d)        

d1 = D()
d1.getA(10)
d1.getB(20)
d1.getC(30)
d1.getD(40)
d1.putA()
d1.putB()
d1.putC()
d1.putD()
