# Operator Overloading

class Point:
    
    def __init__(self,a,b):            #it will Called Automatically when object of class is created
        print("Init Called")
        self.a = a
        self.b = b

    def  __str__(self):                #it will Called When we print the object of class
        print("Str Called") 
        return "[{0},{1}]".format(self.a,self.b)  # Return Value required

    def __add__(self,obj):             #it will Called When addition of two objects
        a = self.a + obj.a
        b = self.b + obj.b
        return Point(a,b)

p1 = Point(10,20)                      #Called __init__ Function        
print(p1)                              #Called  __str__ Fuction
p2 = Point(30,40)                      #Called __init__ Function 
print(p2)                              #Called  __str__ Fuction
print("Addition of Objects : ",p1+p2)  #Called __add__ and __str__ function
