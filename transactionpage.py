from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
from subprocess import call        
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("Main Detail Page")
root.geometry('1270x685')
id = StringVar()
name = StringVar()

transaction_details_frame=LabelFrame(root,text='Transaction Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame.pack(fill=X)
idLabel=Label(transaction_details_frame,text='Your Id',font=('times new roman',15,'bold'),fg='white',bg='grey20')
idLabel.grid(row=0,column=0,padx=20,pady=2)
idEntry=Entry(transaction_details_frame,font=('arial',15),bd=7,width=18,textvariable=id)#,textvariable=rollno)
idEntry.grid(row=0,column=1)

nameLabel=Label(transaction_details_frame,text='Your Name',font=('times new roman',15,'bold'),fg='white',bg='grey20')
nameLabel.grid(row=0,column=2,padx=20,pady=2)
nameEntry=Entry(transaction_details_frame,font=('arial',15),bd=7,width=18,textvariable=name)
nameEntry.grid(row=0,column=3)


typeLabel=Label(transaction_details_frame,text='Type',font=('times new roman',15,'bold'),fg='white',bg='grey20')
typeLabel.grid(row=0,column=4,padx=20,pady=2)
choices=['small','medium','large']
typeEntry=ttk.Combobox(transaction_details_frame,values=choices)
typeEntry.grid(row=0,column=5)


#database System



#logic = SELECT username from login l join transaction t ON l.username=t.username WHERE l.username=

# Frame_Data = Frame(root, bd=12, relief=GROOVE, bg="#e3f4f1")
# Frame_Data.place(x=440 , y=450)
# Frame_Database = Frame(Frame_Data, bd=11, relief=GROOVE)
# Frame_Database.pack(fill=BOTH, expand=True)
# Frame_Database.grid(row=3,column=2)
# def GET_DATA():
# 	con=pymysql.connect(host='localhost',user='root',password='',database='python_app')
# 	cur=con.cursor() 
# 	cur.execute('SELECT * FROM TRANSACTIONS t, LOGIN l WHERE t.username=l.username;')#cur.execute('SELECT * FROM transactions ')where etc
# 	rows=cur.fetchall()
# 	if len(rows)!=0: 
#          for row in rows:
#              Student_table.insert('',END,values=row)
#          con.commit()
#          con.close()

# def FOCUS(e): 
# 	cursor=Student_table.focus()
# 	content=Student_table.item(cursor)
# 	row=content['values']
# 	name.set(row[0])
# 	id.set(row[1])
# # Database Frame
# Frame_Database = Frame(Frame_Data, bg="#e3f4f1", bd=1, relief=GROOVE)
# Frame_Database.grid(row=3,column=2)
# Scroll_X = Scrollbar(Frame_Database, orient=HORIZONTAL)
# Scroll_Y = Scrollbar(Frame_Database, orient=VERTICAL)
# Student_table = ttk.Treeview(Frame_Database, columns=("transaction_id", "transaction_name"), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
# Scroll_X.config(command=Student_table.xview)
# Scroll_X.pack(side=BOTTOM, fill=X)
# Scroll_Y.config(command=Student_table.yview)
# Scroll_Y.pack(side=RIGHT, fill=Y)
# Student_table.heading("transaction_name", text="transaction_name")
# Student_table.heading("transaction_id", text="transaction_id")
# Student_table['show']='headings'
# Student_table.column("transaction_name",width= 100)
# Student_table.column("transaction_id",width= 100)
# Student_table.pack(fill=BOTH, expand=True)
# Student_table.pack(fill=BOTH, expand=True)
# GET_DATA()
# Student_table.bind("<ButtonRelease-1>",FOCUS)
root.mainloop()
