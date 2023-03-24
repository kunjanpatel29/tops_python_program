"""
Inheritance : Creating New Class from an Existing Class is Called Inheritance.
The Object of one Class acquire the property of Object of another class is called Inheritance.
"""

class A:                        # Parent Class
    
    def fun1(self):
        print("Class A Method Called")
   
class B(A):                     # Child Class
    
    def fun2(self):
        print("Class B Method Called")

b1 = B()
b1.fun1()
b1.fun2()


