from tkinter import *       # Tkinter Module
import mysql.connector      # mysql connector library(cmd command = pip install mysql-connector-python)
import tkinter.messagebox as msg  # messagebox is library of tkinter shows the data of written in box

# Connect to database
def create_conn():
    return mysql.connector.connect(   # It is Function to connect with your mysql database
            host="localhost",
            user="root",
            password="",
            database="kunjan"
        )
# print(create_conn()) # Call Function to check code is execute or not

# Inseret data to table in database
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory")
    else:
        conn=create_conn()         # Call Function and store into conn object
        cursor=conn.cursor()
        query="Insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args) # For Execute your query into mysql
        conn.commit()              # Use Commit to save your data permanently to a database table
        conn.close()
        e_fname.delete(0,'end')    # To Delete Data from TextField only
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

# Search Data By ID
def search_data():
    e_fname.delete(0,'end')    # To Delete Data from TextField only
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Search Status","Id Is Mandatory For Search")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()       # fetch all the data from database
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(1,i[2])
                e_email.insert(2,i[3])
                e_mobile.insert(3,i[4])
        else:
            msg.showinfo("Search Status","Id Not Found")
        conn.close()

# Update Data
def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showmsg("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')    # To Delete Data from TextField only
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

# Delete Data
def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')    # To Delete Data from TextField only
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")


root = Tk()                 # object of Tk Class
root.geometry("400x380")    # It will Open Page in size of 400x380
root.title("My Tkinter Demo")  # It will Display Title in web page
root.resizable(width=False,height=False) # It will remove maximize symbol from web page  

# Label Creation and Place in root
l_id=Label(root,text="ID",font=("Arial",15))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",15))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME",font=("Arial",15))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",15))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("Arial",15))
l_mobile.place(x=50,y=250)

# TextField(Entry) Creation
e_id = Entry(root)
e_id.place(x=200,y=50)

e_fname = Entry(root)
e_fname.place(x=200,y=100)

e_lname = Entry(root)
e_lname.place(x=200,y=150)

e_email = Entry(root)
e_email.place(x=200,y=200)

e_mobile = Entry(root)
e_mobile.place(x=200,y=250)

# Button Creation
insert=Button(root,text="INSERT",font=("Arial",10),fg="white",bg="black",command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",font=("Arial",10),fg="white",bg="black",command=search_data)
search.place(x=110,y=300)

update=Button(root,text="UPDATE",font=("Arial",10),fg="white",bg="black",command=update_data)
update.place(x=178,y=300)

delete = Button(root,text="DELETE",font=("Arial",10),fg="white",bg="black",command=delete_data)
delete.place(x=244,y=300)

root.mainloop()  # mainloop is a method on the main window which we execute when we want to run our application.
