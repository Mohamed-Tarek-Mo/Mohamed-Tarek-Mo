from tkinter import *
from tkinter import messagebox
from tkinter import ttk
user_name='admin';user_pass='123456'
casher_name='casher';casher_pass='2468'


'''Center The Window At The Middle Of The Screen'''
def resize_and_center(window2, width, height):
    window2.width = width
    window2.height = height
    screenwidth = window2.winfo_screenwidth()
    screenheight = window2.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    window2.geometry(f'{width}x{height}+{x}+{y}')

'''Centerization'''

'''Start Of The Login Window With Tkinter'''
window2=Tk()

'''The Validation Conditions'''

def check_login():
  if user_field.get()=='' and password_field.get()=='':
    messagebox.showwarning(title='Access Type Error',message="Please Enter The Data")
  elif user_field.get()=='':
     messagebox.showwarning(title='Access Type Error',message="Please Enter Username")
  elif password_field.get()=='':
    messagebox.showwarning(title='Access Type Error',message="Please Enter Password")
  elif x.get()=='':
    messagebox.showwarning(title='Access Type Error',message="You Should Mark 'user' or 'Employee' ")
  elif x.get():
    if user_field.get()!='' and password_field.get()!='':
      if user_field.get()==casher_name and password_field.get()==casher_pass and x.get()=='Employee':
          window2.destroy()
          import gui
          
      elif user_field.get()==casher_name and password_field.get()==casher_pass and x.get()!='Employee':
        messagebox.showerror(title='error Validation',message="Something Is Wrong")
      elif user_field.get()!=casher_name and password_field.get()==casher_pass and x.get()=='Employee':
        messagebox.showerror(title='error Validation',message="Something Is Wrong")
      elif user_field.get()==casher_name and password_field.get()!=casher_pass and x.get()=='Employee':
        messagebox.showerror(title='error Validation',message="Something Is Wrong")
      elif user_field.get()!=casher_name and password_field.get()!=casher_pass and x.get()=='Employee':
        messagebox.showerror(title='error Validation',message="Something Is Wrong")
      if user_field.get()==user_name and password_field.get()==user_pass and x.get()=='Admin':
          window2.destroy()
          import backend
          
        
      if user_field.get()==user_name and password_field.get()==user_pass and x.get()!='Admin':
            messagebox.showerror(title='error Validation',message="Something Is Wrong") 
      elif user_field.get()==user_name and password_field.get()!=user_pass and x.get()=='Admin':
          messagebox.showerror(title='error Validation',message="Something Is Wrong") 
      elif user_field.get()!=user_name and password_field.get()==user_pass and x.get()=='Admin':
            messagebox.showerror(title='error Validation',message="Something Is Wrong") 
      elif user_field.get()!=user_name and password_field.get()!=user_pass and x.get()=='Admin':
            messagebox.showerror(title='error Validation',message="Something Is Wrong") 
    elif user_field.get()!=casher_name or user_field.get()!=user_name and password_field.get()!=casher_pass or password_field.get()!=user_pass:
        messagebox.showwarning(title='Access Type Error',message="Username or password is wrong")

'''The end Of The Validations Code'''

#window2.geometry('1100x700')
window2.resizable(False,False)
window2.title('Login page')
resize_and_center(window2,400,500)



logo=PhotoImage(file='coffee-cup.png')
window2.iconphoto(True,logo)

'''The Icons for UserName And Passwords'''
p1=PhotoImage(file='coffee-shop.png')
'''The End of the Icons'''

login_frame=Frame(
  window2,
  bd=5,
  relief=FLAT,
  padx=5,
)
login_frame.pack(expand=True)

header=Label(
  login_frame,
  text='Cafe System',
  font=("Segoe Print",25),
  fg='gray',
  image=p1,
  compound='top'
)
header.pack(side='top',pady=20)

u1=Label(
  login_frame,
  text='Username',
  font=('Consolas',20),  
)
u1.pack()

user_field=Entry(
  login_frame,
  width=30,
  font=("Consolas",12,'bold')
)
user_field.pack(pady=10)

u2=Label(
  login_frame,
  text='Password',
  font=('Consolas',20)
)
u2.pack()

password_field=Entry(
  login_frame,
  width=30,
  font=("Consolas",12,'bold'),
  show='*'
)
password_field.pack()

x=StringVar()


user=Checkbutton(
  login_frame,
  variable=x,
  onvalue='Admin',
  offvalue='',
  text='Admin',
  padx=20,
  pady=50,font=("Consolas",15)
)
user.pack(side=LEFT)

employee=Checkbutton(
  login_frame,
  variable=x,
  onvalue='Employee',
  text='Employee',
  offvalue='',
  padx=20,pady=50,
  font=("Consolas",15)
)
employee.pack(side=RIGHT)


login=Button(
  login_frame,
  font=("Consolas",15),
  text='Login',
  padx=5,
  pady=5,
  command=check_login
)
login.pack(side='bottom',anchor=CENTER)

window2.mainloop()