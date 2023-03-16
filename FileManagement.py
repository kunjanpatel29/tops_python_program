file = open("hello.txt","w")
file.write("This is File Management demo using python.")
file.close()
print("File Written Successfully")
print("******************************************************")

file = open("hello.txt","r")
print(file.read())
file.close()
print("******************************************************")

file = open("hello.txt","a")
file.write("\nNow this file is appended.")
file.close()
print("File Appended Successfully")
print("******************************************************")

file = open("hello.txt","r")
print(file.read())
file.close()
print("******************************************************")

file = open("hello1.txt","w+")
file.write("This is a file w+ mode using python for read & write data.")
print("Display Cursor is on index number ",file.tell())
file.seek(0) # Set Cursor index to the 0
print(file.read())
file.close()
print("******************************************************")

file = open("hello1.txt","r+")
#file.write("This is a file r+ mode using python.")
print(file.read()) # By Default Cursor is on 1st index.
file.write("\nNow appended text using r+ method.")
file.seek(0)
print(file.read())
file.close()
print("******************************************************")
