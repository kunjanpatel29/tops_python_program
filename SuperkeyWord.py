# Example of SuperKeyword

class ParentClass:

    def parent_method(self):
        print("This is a parent method")
        
class ChildClass(ParentClass):

    def child_method(self):
        print("This is a child method")
        super().parent_method()

obj = ChildClass()
obj.child_method()
