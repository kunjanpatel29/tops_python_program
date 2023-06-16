# Arguments
def fun(fname):
    print(fname + " Patel")

fun("Kunjan")
fun("Sanjay")

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Kunjan", "Patel")
fun("Sanajy")


# Keyword Arguments : You can send arguments with the key = value syntax. Order does not matter
def student_detail(name,rollno,department):
    print("Name is : ",name)

student_detail(department="IT",name="Kunjan",rollno=29)

