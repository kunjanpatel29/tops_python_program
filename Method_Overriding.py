"""
Method Overriding : When there is same method prototype in both base class and derived class
If you call that method Using the object of derived class then derived class method will
be called so you can say that Method of derived class overrides the method of base class. 

"""

class A:

    def show(self):
        print("Show from A")

class B(A):

    def show(self):
        print("Show from B")

class C(B):

    def show(self):
        print("Show from C")

c1 = C()
c1.show()


# Using Super Function

print("\nUsing Super Fuction")
class A:

    def show(self):
        print("Show from A")

class B(A):

    def show(self):
        super().show()           # Super Function 
        print("Show from B")

class C(B):

    def show(self):
        super().show()           # Super Function
        print("Show from C")

c1 = C()
c1.show()


    
