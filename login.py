from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
from subprocess import call
#import pymysql
#import pymysql as mq
import mysql.connector

def reg_page():
    login_window.destroy()
    import register.py

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Feilds Are Required')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='',database="python_app")
            mycursor=con.cursor()
            print("connected to db")
        except:
            messagebox.showerror('Error','Connection Has Not Established Try Again')
            return
    query ='use python_app'
    mycursor.execute(query)
    query='select * from login where username=%s and password=%s'
    mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror('error','Invalid Username Or Password')
    else:
        login_window.destroy()
        messagebox.showinfo('Welcome','Login Is Sucessfull')
        call(["python", "transactionpage.py"])

#FUNCTION
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
#GUI PART
login_window=Tk()
#   login_window.geometry('1968x980+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()
heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),fg='firebrick1',bg='white')
heading.place(x=510,y=120)
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=490,y=200)
usernameEntry.insert(0,'Username')
#username function
usernameEntry.bind('<FocusIn>',user_enter)
frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=490,y=222)
#PASSWORD 
passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=490,y=260)
passwordEntry.insert(0,'Password')
#password function
passwordEntry.bind('<FocusIn>',password_enter)
frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=490,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=720,y=255)
loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=490,y=330)
newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline')
                        ,fg='blue',bg='white',activeforeground='blue',
                        activebackground='white',cursor='hand2',bd=0,command=reg_page)
newaccountButton.place(x=644,y=380)
login_window.mainloop()