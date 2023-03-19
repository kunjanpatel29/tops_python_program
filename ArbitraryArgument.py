# Arbitrary Argument(*,**)

"""
It is Used When user does not know number of argument.
    * - It Create a Tuple - always use in last or second last if ** argument available
    ** - It Create a Dictionary - always use in last
"""

def test(a,b,c,*d,**e):
    print("A : ",a," B : ",b," C : ",c," D : ",d," E : ",e)

test(1,2,3,4,5,6,7,8,9,x=19,y=29,z=36)
