import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox


def add_new_user():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="Grimmijow06",
        database="Hospital"
    )

    cursor = db.cursor()

    sql = "INSERT INTO login (name, password) VALUES (%s, %s)"
    val = (name_entry.get(), key_entry.get())
    cursor.execute(sql, val)
    db.commit()
    x = cursor.rowcount
    messagebox.showinfo("Status", str(x) + " record inserted")


def login():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="Grimmijow06",
        database="Hospital"
    )

    cursor = db.cursor()
    z = cursor.execute("Select * from login")
    if name_entry.get() == '' or key_entry.get() == '':
        messagebox.showerror("Error", "Fill in all fields")
    for i in cursor:
        print(i)
        if name_entry.get() == i[1] and key_entry.get() == i[2]:
            messagebox.showinfo("STATUS", "Access Granted")
            break

    else:
        messagebox.showerror("Error", "Access Denied")


root = Tk()

root.geometry("650x650")
root.title("Hospital Login")

username = Label(root, text="Enter email: ")
username.place(x=10, y=10)
password = Label(root, text="Enter password: ")
password.place(x=10, y=50)

name_entry = Entry(root)
name_entry.place(x=100, y=10)
key_entry = Entry(root, show="*")
key_entry.place(x=100, y=50)

login_btn = Button(root, text="Login", command=login)
login_btn.place(x=10, y=120)
new_user = Button(root, text="Add New User", command=add_new_user)
new_user.place(x=100, y=120)

mainloop()
