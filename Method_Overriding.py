"""
Polymorphism : It means one name many Forms.

** Two Types of Polymorphism ** 

1)Compile Time Polymorphism(Method Overloading): When there is More than one method in a single class having the same
name but different number of arguments and data types that is called Method Overloading.

2)Runtime Polymorphism(Method Overriding) : When there is same method prototype in both base class and derived class
and If you call that method Using the object of derived class then only derived class method will
be called so you can say that Method of derived class overrides the method of base class. 
"""

# Method Overriding Example

class A:                         #Parent Class

    def show(self):
        print("Show from A")

class B(A):                      #Intermediate Class

    def show(self):
        super().show()           #Use Super Function 
        print("Show from B")

class C(B):                      #Child Class
    
    def show(self):
        super().show()           #Use Super Function
        print("Show from C")

c1 = C()
c1.show()


    
