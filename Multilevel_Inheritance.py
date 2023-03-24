"""
Multilevel Inheritance : The features of the Parent class and the child class are further inherited into the new child class is called Multilevel Inheritance.

Parent Class -> Intermediatory Class -> Child Class
GrandFather  ->  Father -> Son

"""

class A:                        # Parent Class

    def getA(self,a):
        self.a = a

    def putA(self):
        print("A : ",self.a)

class B(A):                     # Intermediate class

    def getB(self,b):
        self.b = b

    def putB(self):
        print("B : ",self.b)

class C(B):                     # Child Class

    def getC(self,c):
        self.c = c

    def putC(self):
        print("C : ",self.c)
        
c1 = C()
c1.getA(10)
c1.getB(20)
c1.getC(30)
c1.putA()
c1.putB()
c1.putC()
