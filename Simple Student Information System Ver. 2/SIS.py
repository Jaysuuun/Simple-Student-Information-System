import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql


win = tk.Tk()
win.geometry("1400x900+0+0")
win.title("Simple Student Information System")
win.resizable(False, False)

title_head = tk.Label(win,text="Student Information System",fg=("orange"),font=("Helvetica",40,"bold"),relief=tk.GROOVE,bg="brown")
title_head.pack(side=tk.TOP,fill=tk.X)

frame1 = tk.LabelFrame(win,text="Student Data",relief=tk.RIDGE,font=("Helvetica",25,"bold italic"))
frame1.place(x=20,y=110,width=480,height=600)

disframe = tk.Frame(win,bd=1,relief=tk.GROOVE)
disframe.place(x=530,y=80,width=860,height=800)
header = tk.Label(disframe,text="Student(s) List",font=("Helvetica",25,"bold"),relief=tk.GROOVE,bg="Lightgrey")
header.pack(side=tk.TOP,fill=tk.X)

frame2 = tk.Frame(win,bd=1,relief=tk.GROOVE)
frame2.place(x=23,y=550,width=475,height=32)

frame3 = tk.Frame(disframe,bd=1,relief=tk.GROOVE)
frame3.pack(side=tk.TOP,fill=tk.X)

#=========================================================================================================#
def add_student():

    con = pymysql.connect(host="localhost",user="root",password="",database="ssis")
    curs = con.cursor()
    curs.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s)",(id_entry.get(),fname_ent.get(),MI_ent.get(),lname_ent.get(),gender_ent.get(),year_ent.get(), course_ent.get()))
    con.commit()
    con.close()
    fetch_data()
    clear()

def clear():
    id_entry.delete(0,END)
    fname_ent.delete(0, END)
    lname_ent.delete(0, END)
    MI_ent.delete(0, END)
    gender_ent.set(' ')
    year_ent.set(' ')
    course_ent.set(' ')

def remove_selected():
    selected = Listtable.focus()
    Listtable.item(selected)
    con = pymysql.connect(host="localhost",user="root",password="",database="ssis")
    curs = con.cursor()
    curs.execute("DELETE from data WHERE STUDENTID=%s", (id_entry.get()))
    con.commit()
    con.close()
    fetch_data()
    clear()
  
def edit():
    clear()

    selected = Listtable.focus()
    val = Listtable.item(selected)
    content = val['values']

    IDNUMBER.set(content[0])
    FIRSTNAME.set(content[1])
    MIDDLENAME.set(content[2])
    LASTNAME.set(content[3])
    GENDER.set(content[4])
    YEAR.set(content[5])
    COURSE.set(content[6])
    
def save():
    con = pymysql.connect(host="localhost",user="root",password="",database="ssis")
    curs = con.cursor()
    curs.execute("update data set FIRSTNAME=%s,MIDDLENAME=%s,LASTNAME=%s,GENDER=%s,YEARLEVEL=%s,COURSEID = %s where STUDENTID=%s",(fname_ent.get(),MI_ent.get(),lname_ent.get(),gender_ent.get(),year_ent.get(),course_ent.get(),id_entry.get()))
    con.commit()
    con.close()
    fetch_data()
    clear()

def correct_inpt(inpt):
    if len(inpt)<10:
        return True
    elif inpt == "":
        return True
    else:
        return False

def fetch_data():
    con = pymysql.connect(host = "localhost",user="root",password = "",database = "ssis")
    curs = con.cursor()
    curs.execute("SELECT d.STUDENTID,d.FIRSTNAME,d.MIDDLENAME,d.LASTNAME,d.GENDER,d.YEARLEVEL,d.COURSEID,c.Course FROM data as d INNER JOIN courses as c ON d.COURSEID = c.COURSEID")
    rows = curs.fetchall()
    if len(rows)!=0:
        Listtable.delete(*Listtable.get_children())
        for row in rows:
            Listtable.insert('',tk.END,values=row)
        con.commit()
    con.close()

def searchfun():
    con = pymysql.connect(host = "localhost",user="root",password = "",database = "ssis")
    curs = con.cursor()
    selected = searchcat.get()

    if selected == "Last name":
        curs.execute("SELECT d.STUDENTID,d.FIRSTNAME,d.MIDDLENAME,d.LASTNAME,d.GENDER,d.YEARLEVEL,d.COURSEID,c.Course FROM data as d, courses as c WHERE d.COURSEID = c.COURSEID AND LASTNAME like %s", (searchbar.get()))
        rows = curs.fetchall()
    if selected == "ID Number":
        curs.execute("SELECT d.STUDENTID,d.FIRSTNAME,d.MIDDLENAME,d.LASTNAME,d.GENDER,d.YEARLEVEL,d.COURSEID,c.Course FROM data as d, courses as c WHERE d.COURSEID = c.COURSEID AND STUDENTID like %s", (searchbar.get()))
        rows = curs.fetchall()

    if len(rows)!=0:
        Listtable.delete(*Listtable.get_children())
        for row in rows:
            Listtable.insert('',tk.END,values=row)
        con.commit()
    con.close()

def search():
    for record in Listtable.get_children():
            Listtable.delete(record)

    searchfun()
    
#=================================================================================================#

IDNUMBER = tk.StringVar()
id_number = tk.Label(frame1,text="ID-NO.",font=('Helvetica',20,"bold"))
id_number.grid(row=0,column=0,padx=0,pady=0,sticky= W)
id_eg = tk.Label(frame1,text="eg. 2020-xxxx", font=('Helvetica',15))
id_eg.grid(row=1,column=1,padx=0,pady=5)
id_entry = tk.Entry(frame1,bd=2,font=("Helvetica",15),width=25,textvariable = IDNUMBER)
id_entry.grid(row=0,column=1,padx=0,pady=5)
reg = frame1.register(correct_inpt)
id_entry.config(validate="key",validatecommand=(reg,'%P'))

FIRSTNAME = tk.StringVar()
fname = tk.Label(frame1,text="First name",font=('Helvetica',20,"bold"))
fname.grid(row=2,column=0,padx=0,pady=5,sticky= W)
fname_ent = tk.Entry(frame1,bd=2,font=("Helvetica",15),width=25,textvariable = FIRSTNAME)
fname_ent.grid(row=2,column=1,padx=0,pady=5)

MIDDLENAME = tk.StringVar()
MI = tk.Label(frame1,text="Middle name",font=('Helvetica',20,"bold"))
MI.grid(row=3,column=0,padx=0,pady=5,sticky= W)
MI_ent = tk.Entry(frame1,bd=2,font=("Helvetica",15),width=25,textvariable = MIDDLENAME)
MI_ent.grid(row=3,column=1,padx=0,pady=5)

LASTNAME = tk. StringVar()
lname = tk.Label(frame1,text="Lastname",font=('Helvetica',20,"bold"))
lname.grid(row=4,column=0,padx=0,pady=5,sticky= W)
lname_ent = tk.Entry(frame1,bd=2,font=("Helvetica",15),width=25,textvariable = LASTNAME)
lname_ent.grid(row=4,column=1,padx=0,pady=5)

GENDER = tk.StringVar()
gender = tk.Label(frame1,text="Gender",font=('Helvetica',20,"bold"))
gender.grid(row=5,column=0,padx=0,pady=5,sticky=W)
gender_ent = ttk.Combobox(frame1,font=("Helvetica",15),width=24, state="readonly",textvariable = GENDER)
gender_ent['values']=("Male","Female","Others")
gender_ent.grid(row=5,column=1,padx=0,pady=5)

YEAR = tk.StringVar()
year = tk.Label(frame1,text="Year Level",font=('Helvetica',20,"bold"))
year.grid(row=6,column=0,padx=0,pady=5,sticky= W)
year_ent = ttk.Combobox(frame1,font=("Helvetica",15),width=24, state="readonly",textvariable = YEAR)
year_ent['values']=("1st Year","2nd Year","3rd Year","4th Year","5th Year")
year_ent.grid(row=6,column=1,padx=0,pady=5)

COURSE = tk.StringVar()
course = tk.Label(frame1,text="Course ID",font=('Helvetica',20,"bold"))
course.grid(row=7,column=0,padx=0,pady=5,sticky= W)
course_ent = ttk.Combobox(frame1,font=("Helvetica",15),width=24, state = "readonly",textvariable = COURSE)
course_ent['values'] = ("BSCS","BSIT","BSBIO","BSEd","BSBA","BSIS")
course_ent.grid(row=7,column=1,padx=0,pady=5)

#===========================================================================================#

addbtn= tk.Button(frame2,text="Add Student",bd=1,font=("Helvetica",12),relief=tk.RAISED,command = add_student)
addbtn.grid(row=0,column=0,padx=0,pady=0)

removebtn= tk.Button(frame2,text="Remove Student",bd=1,font=("Helvetica",12),relief=tk.RAISED, command = remove_selected)
removebtn.grid(row=0,column=1,padx=0,pady=0)

editbtn= tk.Button(frame2,text="Edit Student Information",bd=1,font=("Helvetica",12),relief=tk.RAISED,command = edit)
editbtn.grid(row=0,column=2,padx=0,pady=0)

savebtn= tk.Button(frame2,text="Save",bd=1,font=("Helvetica",12),relief=tk.RAISED,width=7, command = save)
savebtn.grid(row=0,column=3,padx=0,pady=0)
#===========================================================================================#

searchby = tk.Label(frame3,text="Search by",font=("Helvetica",18))
searchby.grid(row=0,column=0,padx=0,pady=0)

SEARCH = tk.StringVar()
searchcat = ttk.Combobox(frame3,font=("Helvetica",15),state="readonly",width=10,textvariable=SEARCH)
searchcat['values'] = ("Last name","ID Number")
searchcat.current(0)
searchcat.grid(row=0,column=1,padx=0,pady=0)
Searchbtn = tk.Button(frame3,text="Search",font=("Helvetica",13),width = 11, relief=tk.RAISED, command=search)
Searchbtn.grid(row=0,column=3,padx=0,pady=0)
searchbar = tk.Entry(frame3,bd=2,font=("Helvetica",15),width=33)
searchbar.grid(row=0,column=2,padx=0,pady=5)

Showbtn = tk.Button(frame3,text="Show All",font=("Helvetica",13),width = 13, relief=tk.RAISED, command=fetch_data)
Showbtn.grid(row=0,column=4,padx=0,pady=0)

#===========================================================================================================#
frame4 = tk.Frame(disframe,bd=7,relief=tk.SUNKEN)
frame4.pack(fill=tk.BOTH,expand=True)

vscroll = tk.Scrollbar(frame4,orient=tk.VERTICAL)
hscroll = tk.Scrollbar(frame4,orient=tk.HORIZONTAL)

Listtable = ttk.Treeview(frame4,columns=("ID NUMBER","FIRST NAME","MIDDLE NAME","LAST NAME","GENDER","YEAR LEVEL","COURSEID","COURSE"),yscrollcommand=vscroll.set,xscrollcommand=hscroll.set)

vscroll.config(command=Listtable.yview)
hscroll.config(command=Listtable.xview)

vscroll.pack(side=tk.RIGHT,fill=tk.Y)
hscroll.pack(side=tk.BOTTOM,fill=tk.X)

Listtable.heading("ID NUMBER",text="ID NUMBER")
Listtable.heading("FIRST NAME",text="FIRST NAME")
Listtable.heading("LAST NAME",text="LAST NAME")
Listtable.heading("MIDDLE NAME",text="MIDDLE NAME")
Listtable.heading("GENDER",text="GENDER")
Listtable.heading("YEAR LEVEL",text="YEAR LEVEL")
Listtable.heading("COURSEID",text="COURSE ID")
Listtable.heading("COURSE",text="COURSE")

Listtable['show'] = 'headings'

Listtable.column("ID NUMBER",width=100)
Listtable.column("FIRST NAME",width=150)
Listtable.column("LAST NAME",width=150)
Listtable.column("MIDDLE NAME",width=150)
Listtable.column("GENDER",width=100)
Listtable.column("YEAR LEVEL",width=100)
Listtable.column("COURSEID",width=100)
Listtable.column("COURSE",width=350)

fetch_data()

Listtable.pack(fill=tk.BOTH,expand=True)
#============================================================================================#

win.mainloop()
