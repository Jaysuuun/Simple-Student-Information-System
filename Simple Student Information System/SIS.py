import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter as Tkinter
from csv import DictWriter
import os
from tkinter import messagebox

win = tk.Tk()
win.geometry("1200x720+0+0")
win.title("Simple Student Information System")
win.resizable(False, False)

title_head = tk.Label(win,text="Ilimintary Skul",fg=("orange"),font=("Helvetica",35,"bold"),relief=tk.GROOVE,bg="brown")
title_head.pack(side=tk.TOP,fill=tk.X)

frame1 = tk.LabelFrame(win,text="Student Data",relief=tk.RIDGE,font=("Helvetica",20,"bold italic"))
frame1.place(x=20,y=90,width=400,height=400)

disframe = tk.Frame(win,bd=1,relief=tk.GROOVE)
disframe.place(x=450,y=65,width=720,height=640)
header = tk.Label(disframe,text="Student(s) List",font=("Helvetica",20,"bold"),relief=tk.GROOVE,bg="Lightgrey")
header.pack(side=tk.TOP,fill=tk.X)

frame2 = tk.Frame(win,bd=1,relief=tk.GROOVE)
frame2.place(x=20,y=500,width=400,height=28)

frame3 = tk.Frame(disframe,bd=1,relief=tk.GROOVE)
frame3.pack(side=tk.TOP,fill=tk.X)

csv_database = 'Student(s)List.csv'
#===========================================================================================================================#
frame4 = tk.Frame(disframe,bd=7,relief=tk.SUNKEN)
frame4.pack(fill=tk.BOTH,expand=True)

vscroll = tk.Scrollbar(frame4,orient=tk.VERTICAL)
hscroll = tk.Scrollbar(frame4,orient=tk.HORIZONTAL)

Listtable = ttk.Treeview(frame4,columns=("ID NUMBER","FIRST NAME","LAST NAME","MIDDLE NAME","GENDER","COURSE","YEAR LEVEL"),yscrollcommand=vscroll.set,xscrollcommand=hscroll.set)

vscroll.config(command=Listtable.yview)
hscroll.config(command=Listtable.xview)

vscroll.pack(side=tk.RIGHT,fill=tk.Y)
hscroll.pack(side=tk.BOTTOM,fill=tk.X)

Listtable.heading("ID NUMBER",text="ID NUMBER")
Listtable.heading("FIRST NAME",text="FIRST NAME")
Listtable.heading("LAST NAME",text="LAST NAME")
Listtable.heading("MIDDLE NAME",text="MIDDLE NAME")
Listtable.heading("GENDER",text="GENDER")
Listtable.heading("COURSE",text="COURSE")
Listtable.heading("YEAR LEVEL",text="YEAR LEVEL")

Listtable['show'] = 'headings'

Listtable.column("ID NUMBER",width=100)
Listtable.column("FIRST NAME",width=150)
Listtable.column("LAST NAME",width=150)
Listtable.column("MIDDLE NAME",width=150)
Listtable.column("GENDER",width=100)
Listtable.column("COURSE",width=100)
Listtable.column("YEAR LEVEL",width=100)



global count
count = 0

Listtable.pack(fill=tk.BOTH,expand=True)


#===========================================================================================================================#
def add_student():
    global count
    global csv_database
    with open(csv_database,'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=['ID Number','First Name','Last Name','Middle Name','Gender','Course','Year Level'])

        if os.stat(csv_database).st_size==0: 
            DictWriter.writeheader(dict_writer)

        dict_writer.writerow({'ID Number':id_entry.get(),'First Name':fname_ent.get(),'Last Name':lname_ent.get(),'Middle Name':MI_ent.get(),'Gender':gender_ent.get(),'Course':course_ent.get(),'Year Level':year_ent.get()})

    
    Listtable.insert(parent = '',index='end',iid=count,text="",values =(id_entry.get(),fname_ent.get(),lname_ent.get(),MI_ent.get(),gender_ent.get(),course_ent.get(),year_ent.get()))

    count += 1
    
    id_entry.delete(0,END)
    fname_ent.delete(0, END)
    lname_ent.delete(0, END)
    MI_ent.delete(0, END)
    gender_ent.set(' ')
    course_ent.delete(0, END)
    year_ent.set(' ')



def remove_selected():
    x = Listtable.selection()
    for record in x:
        Listtable.delete(record)

def edit():
    id_entry.delete(0,END)
    fname_ent.delete(0, END)
    lname_ent.delete(0, END)
    MI_ent.delete(0, END)
    gender_ent.set(' ')
    course_ent.delete(0, END)
    year_ent.delete(0, END)

    selected = Listtable.focus()

    values = Listtable.item(selected,'values')

    id_entry.insert(0,values[0])
    fname_ent.insert(0, values[1])
    lname_ent.insert(0, values[2])
    MI_ent.insert(0, values[3])
    gender_ent.insert(0,values[4])
    course_ent.insert(0, values[5])
    year_ent.insert(0, values[6])

def save():
    selected = Listtable.focus()
    Listtable.item(selected,text="",values =(id_entry.get(), fname_ent.get(),lname_ent.get(),MI_ent.get(),gender_ent.get(),course_ent.get(),year_ent.get()))

    id_entry.delete(0,END)
    fname_ent.delete(0, END)
    lname_ent.delete(0, END)
    MI_ent.delete(0, END)
    gender_ent.set(' ')
    course_ent.delete(0, END)
    year_ent.set(' ')

def correct_inpt(inpt):
    if inpt.isdigit()and len(inpt)<9:
        return True
    elif inpt == "":
        return True
    else:
        return False
    
#===========================================================================================================================#

#=============================================================================================#
id_ent_var = tk.StringVar()
id_number = tk.Label(frame1,text="ID-NO.",font=('Helvetica',15,"bold"))
id_number.grid(row=0,column=0,padx=0,pady=0,sticky= W)
id_eg = tk.Label(frame1,text="eg. 12345678", font=('Helvetica',10))
id_eg.grid(row=1,column=1,padx=0,pady=5)
id_entry = tk.Entry(frame1,bd=2,font=("Helvetica",13),width=23,textvariable = id_ent_var)
id_entry.grid(row=0,column=1,padx=0,pady=5)
reg = frame1.register(correct_inpt)
id_entry.config(validate="key",validatecommand=(reg,'%P'))


fname = tk.Label(frame1,text="First name",font=('Helvetica',15,"bold"))
fname.grid(row=2,column=0,padx=0,pady=5,sticky= W)
fname_ent = tk.Entry(frame1,bd=2,font=("Helvetica",13),width=23)
fname_ent.grid(row=2,column=1,padx=0,pady=5)


lname = tk.Label(frame1,text="Lastname",font=('Helvetica',15,"bold"))
lname.grid(row=3,column=0,padx=0,pady=5,sticky= W)
lname_ent = tk.Entry(frame1,bd=2,font=("Helvetica",13),width=23)
lname_ent.grid(row=3,column=1,padx=0,pady=5)


MI = tk.Label(frame1,text="Middle name",font=('Helvetica',15,"bold"))
MI.grid(row=4,column=0,padx=0,pady=5,sticky= W)
MI_ent = tk.Entry(frame1,bd=2,font=("Helvetica",13),width=23)
MI_ent.grid(row=4,column=1,padx=0,pady=5)


gender = tk.Label(frame1,text="Gender",font=('Helvetica',15,"bold"))
gender.grid(row=5,column=0,padx=0,pady=5,sticky=W)
gender_ent = ttk.Combobox(frame1,font=("Helvetica",13),width=21, state="readonly")
gender_ent['values']=("Male","Female","Others")
gender_ent.grid(row=5,column=1,padx=0,pady=5)


course = tk.Label(frame1,text="Course",font=('Helvetica',15,"bold"))
course.grid(row=6,column=0,padx=0,pady=5,sticky= W)
course_ent = tk.Entry(frame1,bd=2,font=("Helvetica",13),width=23)
course_ent.grid(row=6,column=1,padx=0,pady=5)


year = tk.Label(frame1,text="Year Level",font=('Helvetica',15,"bold"))
year.grid(row=7,column=0,padx=0,pady=5,sticky= W)
year_ent = ttk.Combobox(frame1,font=("Helvetica",13),width=21, state="readonly")
year_ent['values']=("1st Year","2nd Year","3rd Year","4th Year","5th Year")
year_ent.grid(row=7,column=1,padx=0,pady=5)

#===========================================================================================#

#===========================================================================================#
addbtn= tk.Button(frame2,text="Add Student",bd=1,font=("Helvetica",10),relief=tk.RAISED,command = add_student)
addbtn.grid(row=0,column=0,padx=0,pady=0)

removebtn= tk.Button(frame2,text="Remove Student",bd=1,font=("Helvetica",10),relief=tk.RAISED, command = remove_selected)
removebtn.grid(row=0,column=1,padx=0,pady=0)

editbtn= tk.Button(frame2,text="Edit Student Information",bd=1,font=("Helvetica",10),relief=tk.RAISED,command = edit)
editbtn.grid(row=0,column=3,padx=0,pady=0)

savebtn= tk.Button(frame2,text="Save",bd=1,font=("Helvetica",10),relief=tk.RAISED,width=7, command = save)
savebtn.grid(row=0,column=4,padx=0,pady=0)
#==========================================================================================#

#=========================================================================================#

searchby = tk.Label(frame3,text="Search by",font=("Helvetica",12))
searchby.grid(row=0,column=0,padx=0,pady=0)

searchcat = ttk.Combobox(frame3,font=("Helvetica",12),state="readonly",width=10)
searchcat['values'] = ("First name","Last name","Middle name","ID Number")
searchcat.grid(row=0,column=1,padx=0,pady=0)

Searchbtn = tk.Button(frame3,text="Search",font=("Helvetica",12),width = 13, relief=tk.RAISED)
Searchbtn.grid(row=0,column=3,padx=0,pady=0)
searchbar = tk.Entry(frame3,bd=2,font=("Helvetica",13),width=29)
searchbar.grid(row=0,column=2,padx=0,pady=5)

Showbtn = tk.Button(frame3,text="Show All",font=("Helvetica",12),width = 13, relief=tk.RAISED)
Showbtn.grid(row=0,column=4,padx=0,pady=0)

#============================================================================================#

#=============================================================================================#


#=============================================================================================#
win.mainloop()
