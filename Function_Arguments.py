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

# Default Argument: If we call the function without argument, it uses the default value
def fun(country = "India"):
    print("I am from " + country)

fun("Brazil")
fun()
fun("USA")

# Passing a List as an Argument
def my_function(car):
  for x in car:
    print(x)

cars = ["Swift","BMW","Audi"]

my_function(cars)
