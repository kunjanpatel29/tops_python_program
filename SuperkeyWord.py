# Example of SuperKeyword

""" class ParentClass:

    def parent_method(self):
        print("This is a parent method")
        
class ChildClass(ParentClass):

    def parent_method(self):
        print("Super Keyword Example")
        super().parent_method()
        
    def child_method(self):
        print("This is a child method")
        super().parent_method()

obj = ChildClass()
obj.child_method()
obj.parent_method()
"""

class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):

    def __init__(self,name,id,lang):
        self.name = name
        self.id = id
        self.lang = lang
    
