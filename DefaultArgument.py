# Default Argument

"""
    If not Put argument at calling time then its taken from default argument.
    Default argument order will be right to left means last to first order.
"""

def test(a=45,b=36,c=29,d=15):  # Given Default Argument
    print("A : ",a," B : ",b," C : ",c," D : ",d)

test(1,2,3,4)       # Print Parameter Value
test(1,2,3)         # Value of d is taken from default argument
test(1,2)         
test(1)
test()              
test(b=100,d=200)   # KeyWord Argument
