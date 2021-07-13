import sqlite3
import sys                         # for forcefully close application
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Set Connection with Database
def connection():
    try:
        conn = sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn


def verifier():
    a = b = c = d = e = f = 0
    if not student_name.get():
        # t1.insert(END,"!! Student name is required \n")
        a = 1
    if not roll_no.get():
        # t1.insert(END,"!! Roll no is required \n")
        b = 1
    if not branch.get():
        # t1.insert(END,"!! Branch is required \n")
        c = 1
    if not phone.get():
        # t1.insert(END,"!! Phone number is requrired \n")
        d = 1
    if not father.get():
        # t1.insert(END,"!! Father name is required \n")
        e = 1
    if not address.get():
        # t1.insert(END,"!! Address is Required \n")
        f = 1
    if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1:
        t1.insert(END, "!! All entries are required \n")
        return 1
    else:
        return 0


def add_student():
    ret = verifier()
    if ret == 0:
        # check connection with database
        conn = connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,"
                    "FATHER TEXT,ADDRESS TEXT)")
        roll = int(roll_no.get())
        cur.execute("select ROLL_NO from STUDENTS")

        # Fetch all data of table
        data = cur.fetchall()
        flag = False
        for row in data:
            if row[0] == roll:
                flag = True
        if not flag:
            cur.execute("insert into STUDENTS values(?,?,?,?,?,?)", (
                student_name.get(), int(roll_no.get()), branch.get(), int(phone.get()), father.get(), address.get()))
            conn.commit()
            conn.close()
            t1.insert(END, "ADDED SUCCESSFULLY\n")
        else:
            t1.insert(END, "THIS ROLL NUMBER ALREADY IN THE DATABASE\n")

# Function to view all students in database
def view_student():
    conn = connection()
    cur = conn.cursor()
    cur.execute("select * from STUDENTS")
    data = cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END, str(i) + "\n")
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

# Function to delete any student from table
def delete_student():
    if not roll_no.get():
        t1.insert(END, "Roll no must be entered\n")
    else:
        ret = 0
        if ret == 0:
            conn = connection()
            cur = conn.cursor()
            roll = int(roll_no.get())
            cur.execute("select ROLL_NO from STUDENTS")
            data = cur.fetchall()
            flag = False
            for row in data:
                if row[0] == roll:
                    flag = True
            if not flag:
                t1.insert(END, "THIS USER IS NOT AVAILABLE\n")
            else:
                cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?", (int(roll_no.get()),))
                conn.commit()
                conn.close()
                t1.insert(END, "SUCCESSFULLY DELETED THE USER\n")

# Function to update details of any student from table
def update_student():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,ROLL_NO=?,BRANCH=?,PHONE_NO=?,FATHER=?,ADDRESS=? where ROLL_NO=?", (
            student_name.get(), int(roll_no.get()), branch.get(), int(phone.get()), father.get(), address.get(),
            int(roll_no.get())))
        conn.commit()
        conn.close()
        t1.insert(END, "UPDATED SUCCESSFULLY\n")

# Function to close application
def clse():
    sys.exit()

# Deletes the text in text area
def delete_text():
    t1.delete("1.0", "end")

# Deletes the entries
def delete_entries():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')

# Sorts the table according to name
def sortname():
    # For sorting purpose
    root.name += 1
    conn = connection()
    cur = conn.cursor()
    if root.name % 2 == 1:
        cur.execute("select * from STUDENTS order by NAME ASC")
    else:
        cur.execute("select * from STUDENTS order by NAME DESC")
    data = cur.fetchall()
    conn.close()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

# Sorts the table according to roll no.
def sortroll_no():
    root.roll += 1
    conn = connection()
    cur = conn.cursor()
    if root.roll % 2 == 1:
        cur.execute("select * from STUDENTS order by ROLL_NO ASC")
    else:
        cur.execute("select * from STUDENTS order by ROLL_NO DESC")
    data = cur.fetchall()
    conn.close()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))


# Sorts the table according to branch
def sortbranch():
    root.branch += 1
    conn = connection()
    cur = conn.cursor()
    if root.branch % 2 == 1:
        cur.execute("select * from STUDENTS order by BRANCH ASC")
    else:
        cur.execute("select * from STUDENTS order by BRANCH DESC")
    data = cur.fetchall()
    conn.close()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))


# Sorts the table according to phone no.
def sortphone():
    root.phone += 1
    conn = connection()
    cur = conn.cursor()
    if root.phone % 2 == 1:
        cur.execute("select * from STUDENTS order by PHONE_NO ASC")
    else:
        cur.execute("select * from STUDENTS order by PHONE_NO DESC")
    data = cur.fetchall()
    conn.close()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))


# Sorts the table according to father name
def sortfather():
    root.father += 1
    conn = connection()
    cur = conn.cursor()
    if root.father % 2 == 1:
        cur.execute("select * from STUDENTS order by FATHER ASC")
    else:
        cur.execute("select * from STUDENTS order by FATHER DESC")
    data = cur.fetchall()
    conn.close()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))


# Sorts the table according to address
def sortaddress():
    root.address += 1
    conn = connection()
    cur = conn.cursor()
    if root.address % 2 == 1:
        cur.execute("select * from STUDENTS order by ADDRESS ASC")
    else:
        cur.execute("select * from STUDENTS order by ADDRESS DESC")
    data = cur.fetchall()
    conn.close()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(data)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12",
                     values=(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))


"""
def show_table():
    conn = connection()
    cur = conn.cursor()
    nme = search.get()
    cur.execute("select * from STUDENTS where NAME = (?)", (nme,))
    lst = cur.fetchall()
    for item in treev.get_children():
        treev.delete(item)
    total_rows = len(lst)
    for i in range(total_rows):
        treev.insert("", 'end', text="L12", values=(lst[i][0], lst[i][1], lst[i][2], lst[i][3], lst[i][4], lst[i][5]))
    conn.close()
"""

if __name__ == "__main__":
    root = tk.Tk()
    # setting title
    root.title("Student Management System")
    root.geometry("1550x800")
    root.resizable(width=True, height=True)
    root.state('zoomed')

    root.name = 0
    root.roll = 0
    root.branch = 0
    root.phone = 0
    root.father = 0
    root.address = 0

    student_name = StringVar()
    roll_no = StringVar()
    branch = StringVar()
    phone = StringVar()
    father = StringVar()
    address = StringVar()
    search = StringVar()

    ttk.Label(root, text="Student Management System").pack()

    # Create Panedwindow
    panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # First frame that is left side frame for entry and buttons
    fram1 = ttk.Frame(panedwindow, width=80, height=300, relief=SUNKEN)
    # Second frame that is left side frame to show tables and text
    fram2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)

    # Create Panedwindow
    panedwindow.add(fram1, weight=1)
    panedwindow.add(fram2, weight=5)

    panedwindow2 = ttk.Panedwindow(fram2, orient=VERTICAL)
    panedwindow2.pack(fill=BOTH, expand=True)

    # Create Frams under the frame that is like sub frames
    fram3 = ttk.Frame(panedwindow2, width=50, height=100, relief=SUNKEN)
    fram4 = ttk.Frame(panedwindow2, width=50, height=100, relief=SUNKEN)
    panedwindow2.add(fram3, weight=3)
    panedwindow2.add(fram4, weight=1)

    # Entries and Buttons

    label1 = Label(fram1, text="Student name:")
    label1.place(x=3, y=10)

    label2 = Label(fram1, text="Roll no:")
    label2.place(x=3, y=40)

    label3 = Label(fram1, text="Branch:")
    label3.place(x=3, y=70)

    label4 = Label(fram1, text="Phone Number:")
    label4.place(x=3, y=100)

    label5 = Label(fram1, text="Father Name:")
    label5.place(x=3, y=130)

    label6 = Label(fram1, text="Address:")
    label6.place(x=3, y=160)

    e1 = Entry(fram1, textvariable=student_name)
    e1.place(x=100, y=10, width=200)

    e2 = Entry(fram1, textvariable=roll_no)
    e2.place(x=100, y=40, width=200)

    e3 = Entry(fram1, textvariable=branch)
    e3.place(x=100, y=70, width=200)

    e4 = Entry(fram1, textvariable=phone)
    e4.place(x=100, y=100, width=200)

    e5 = Entry(fram1, textvariable=father)
    e5.place(x=100, y=130, width=200)

    e6 = Entry(fram1, textvariable=address)
    e6.place(x=100, y=160, width=200)

    widget_var = tk.StringVar()
    combobox = ttk.Combobox(fram3, textvariable=widget_var, width=40)
    combobox.place(x=10, y=5)
    combobox['values'] = ('name', 'roll_no', 'branch', ' phone_no', 'father', 'address')
    combobox.current(0)

    e7 = Entry(fram3, textvariable=search, width=50)
    e7.place(x=280, y=5, width=500)

    ttk.Label(fram4, text="Logs").pack()
    t1 = Text(fram4, width=170, height=20, bg='#fccfe6')
    t1.place(x=1, y=20)

    # Button for clear entries
    b0 = Button(fram1, text="CLEAR ENTRIES", command=delete_entries, width=40, bg='#b8fcf5')
    b0.place(x=3, y=605, width=315)

    # Button for clear text
    b1 = Button(fram1, text="CLEAR TEXT", command=delete_text, width=40, bg='#b8fcf5')
    b1.place(x=3, y=630, width=315)

    # Button to add student
    b2 = Button(fram1, text="ADD STUDENT", command=add_student, width=40, bg='#b8fcf5')
    b2.place(x=3, y=655, width=315)

    # Button to view all students
    b3 = Button(fram1, text="VIEW ALL STUDENTS", command=view_student, width=40, bg='#b8fcf5')
    b3.place(x=3, y=680, width=315)

    # Button to delete a student
    b4 = Button(fram1, text="DELETE STUDENT", command=delete_student, width=40, bg='#b8fcf5')
    b4.place(x=3, y=705, width=315)

    # Button to update info of student
    b5 = Button(fram1, text="UPDATE INFO", command=update_student, width=40, bg='#b8fcf5')
    b5.place(x=3, y=730, width=315)

    # Button to close application
    b6 = Button(fram1, text="CLOSE", command=clse, width=40, bg='#b8fcf5')
    b6.place(x=3, y=755, width=315)

    # b7 = Button(fram3, text="SEARCH", command=show_table(), width=40, bg='#fad778')
    # b7.place(x=810, y=3, width=100)

    # Treeview to show details of all students or selected students in treeview
    treev = ttk.Treeview(fram3, selectmode='browse')
    treev.place(x=10, y=30, height=550)

    # Vertical scroll bar
    verscrlbar = ttk.Scrollbar(fram3, orient="vertical", command=treev.yview)
    verscrlbar.pack(side='right', fill='y')
    treev.configure(yscrollcommand=verscrlbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6")

    treev['show'] = 'headings'

    # Treeview columns
    treev.column("1", width=170, anchor='c')
    treev.column("2", width=120, anchor='c')
    treev.column("3", width=80, anchor='c')
    treev.column("4", width=150, anchor='c')
    treev.column("5", width=200, anchor='c')
    treev.column("6", width=450, anchor='c')

    treev.heading("1", text="Name", command=sortname)
    treev.heading("2", text="Roll_no", command=sortroll_no)
    treev.heading("3", text="Branch", command=sortbranch)
    treev.heading("4", text="Phone_no", command=sortphone)
    treev.heading("5", text="Father", command=sortfather)
    treev.heading("6", text="Address", command=sortaddress)

    root.mainloop()
