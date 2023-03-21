"""
    Class - It is a group of different types of variables and functions.
    Object - It is an Instance of a class.
    Self - It can refer to the Current Object.
"""

# Class is Created
class Student:

    def getData(self,fname,lname):          # Method1 is Created
        self.fname = fname
        self.lname = lname
        
    def putData(self):                      # Method2 is Created
        print("First Name: ",self.fname)    
        print("Last Name:",self.lname)

s1 = Student()  # Object is created

# Called a Method
s1.getData("Kunjan","Patel") 
s1.putData() 
