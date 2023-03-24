# Operator Overloading

class Point:

    def __init__(self,a,b):
        print("Init Called")
        self.a = a
        self.b = b

    def  __str__(self):
        print("Str Called")
        return "[{0},{1}]".format(self.a,self.b)

    def __add__(self,obj):
        a = self.a + obj.a
        b = self.b + obj.b
        return Point(a,b)
        

p1 = Point(10,20)
print(p1)
p2 = Point(30,40)
print(p2)
print("Addition of Objects : ",p1+p2)
