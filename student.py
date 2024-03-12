from tkinter import *
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='1' and passwordEntry.get()=='1':
        messagebox.showinfo('success','welcome')
        win.destroy()
        import sms

    else:
        messagebox.showerror('Error','please enter correct credentials')
    

win=Tk()
win.geometry("500x700+0+0")
win.title("LOGIN SYSTEM OF STUDENT MANAGEMENT SYSTEM")

loginFrame=Frame(win)
loginFrame.place(x=400,y=150)

usernameLabel=Label(loginFrame,text='username',font=('times new roman',30,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',30,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordLabel=Label(loginFrame,text='password',font=('times new roman',30,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',30,'bold'),bd=5)
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='login',font=('times new roman',20,'bold'),bd=15,width=15,bg='cornflowerblue',command=login)
loginButton.grid(row=3,column=1,pady=10)

win.mainloop()


