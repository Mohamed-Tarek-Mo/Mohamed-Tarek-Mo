from tkinter import*  
from tkinter import ttk
from tkinter import messagebox
import connect_data 

#--------The Area Of Functions----------

def tree(tree3):
#---------------------TreeView Results-------------
  tree3.configure(height=14)
#-------------------creation columns---------------
  tree3['columns']=('Name','Quantity','Price')
#---------------columns_2----------------
  tree3.column('#0',width=0,stretch=NO)
  tree3.column('Name',anchor=CENTER,width=165)
  tree3.column('Quantity',anchor=CENTER,width=130)
  tree3.column('Price',anchor=CENTER,width=130)
#---------------headings---------------
  tree3.heading('Name',text='Name',anchor=CENTER,)
  tree3.heading('Quantity',text='Quantity',anchor=CENTER)
  tree3.heading('Price',text='Price',anchor=CENTER)
#----------the End Of Headings----------
  tree3.pack(pady=5)
#--------------------


#----------------The Start Of The delete_item-------------
def delete_items():
  pass
#----------------The end Of The delete_items---------------

#-------------The Start Of The Exit Items------------------
def Exit():
    window.destroy()
#-------------The End Of The Exit Button--------------------


#------------Center The Window At The Middle Of The Screen-----------------
def resize_and_center(window, width, height):
    window.width = width
    window.height = height
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    window.geometry(f'{width}x{height}+{x}+{y}')
#-----------------The ENd Of Center--------------------------------------------

#-----------The Start Of The Tkinter Window (gui.py)---------------

window=Tk()


#------------------The Start Of TreeView Style------------------

style=ttk.Style()
style.theme_use('clam')
style.configure(
  "Treeview",
  background='silver',
  foreground='black',
  rowheight=25,
  fieldbackground='silver'
)
 
style.map(
  "Treeview",
  background=[('selected','green')]
)


#---------------------------Show All Data In The Start----------------



#---------------The start Of The Confirm Window Function -----------------

#-----------The Back Icon In The Back_Button-------------
p=PhotoImage(file='back.png')
#--------------------------------------------------------

#----------------------The go back function----------------



#---------------------The Declartion----------------------

#The Global variable 'count' in Confirm window  
count=1
#---------------------

def confirm_window():
#------top------
#---------------------The Validation Confirm-----------------
  if len(order.get_children())==0:
    messagebox.showinfo(title='',message='There Are No Orders To Show')
    return
#-------------------------------------------------------------------
  global count
  w1=Toplevel()
  w1.title("The Order")
  w1.resizable(False,False)
#--------------------------

#------The Confirm Frame------
  f1=Frame(
    w1
  )
  f1.pack(side='top')
#-----The End Of The Frame-----

#-----The code Of Declare The ScrollBar-------
  yscroll=Scrollbar(f1,orient=VERTICAL)
  yscroll.pack(side=RIGHT,fill=Y)
#-----------The End-----------

#--------The Header Label -----------
  head_1=Label(
    f1,
    font=('Segoe Print',25,'bold'),
    text=f'The Reciept #{count}',
    bd=2,
    relief=GROOVE,
    bg="#c9b98b",
  )

#-----------The Resize function for centering the Window----------
  resize_and_center(w1,430,542)
#--------------------------------------------

#--------------------------------------------
  head_1.pack(side='top',anchor=CENTER,fill=BOTH,expand=True)
#-------The End Of The Header Label---------

#-----------The tree view code-----------------  
  tree3=ttk.Treeview(
    f1,
    yscrollcommand=yscroll.set,
    )
  yscroll.configure(command=tree3.yview)
  tree(tree3)
  count+=1
#---------------the end of it--------------------

#-----------------The Back Button----------------
  Button(
    w1,
    text='Return',
    image=p,
    compound='right',
    padx=10,
    font=('Consolas',15,'bold'),
    relief=GROOVE,
    bg='#c9b98b',
    command=lambda:go_back()
  ).pack(side='top',fill=BOTH,expand=True)

#--------The Back Function------
  def go_back():
    w1.destroy()
    order.delete(*order.get_children())
    total_label.delete(0,END)
    total_label.insert(0,0)
#---------ENd Of It------------

#--------The Begin of Showing Reciept--------

  for value in order.get_children():
    row=order.item(value)['values']
    tree3.insert(parent='',text='',index='end',values=(row[0],row[1],row[2]))

#---------------The End Of The Confirm Function-----------------------


#-----------------The Start Of Total Price Function------------------

def total_price():
  c=0
  for value in order.get_children():
    row=order.item(value)['values']
    c+=row[2]*row[1]
  total_label.delete(0,END)
  total_label.insert(0,str(c))
  total_label.configure(justify=CENTER,fg='black')
#-----------------------The End Of Total Price Function---------------

#----------------------The Start Of function Show_Drinks--------------

num=1
def show_drinks(kind):
  global num
  c=connect_data.filter2(kind)
  if kind=='Hot Drinks':
    num=1
    for i in menu.get_children():
      menu.delete(i)
    for i in range(len(c)):
      menu.insert(parent='',index='end',iid=num,text='',values=(num,c[i][1],c[i][2],c[i][3]))
      num+=1
    num=0
  elif kind=='Cold Drinks':
    num=1
    for i in menu.get_children():
      menu.delete(i)
    for i in range(len(c)):
      menu.insert(parent='',index='end',iid=num,text='',values=(num,c[i][1],c[i][2],c[i][3]))
      num+=1
    num=0
  elif kind=='Sweets':
    num=1
    for i in menu.get_children():
      menu.delete(i)
    for i in range(len(c)):
      menu.insert(parent='',index='end',iid=num,text='',values=(num,c[i][1],c[i][2],c[i][3]))
      num+=1
    num=0
#--------------------The End Of The Show Drinks Function-------------------------------------------


#--------------------The Start Of The Add Function--------------------

def add():
  l=list()
  v=menu.item(menu.focus())['values'] # the focused
  if len(order.get_children())==0:
    order.insert(parent='',index='end',text='',values=(v[1],1,v[2]))
  else:
    for row in order.get_children():# the rows 
       if order.item(row)['values'][0]==v[1]:
        order.item(row,text='',values=(
          order.item(row)['values'][0],
          order.item(row)['values'][1]+1,
          order.item(row)['values'][2]
          )
        )
        print(order.item(row)['values'][1])
        break
    else:
        order.insert(parent='',index='end',text='',values=(v[1],1,v[2]))
#-------------------------The End Of fucken Add Function----------------------


#---------------------------The Start Of Remove Function------------------------

def remove():   
  #v=order.item(menu.focus())['values'] # the focused
  
  for row in order.selection():# the rows 
      order.item(row,text='',values=(
      order.item(row)['values'][0],
      order.item(row)['values'][1]-1,
      order.item(row)['values'][2]
      )   
    )
      if order.item(row)['values'][1]==0:
        messagebox.showwarning(title='Warning Empty Record',message='The Record Is Empty')
        order.delete(row)
        break

#----------------------------The End Of Remove Function----------------      


#--------------The Start Of Clear Message-----------------------------

def clear():
  if messagebox.askokcancel(title='Clear Order',message='Do You Want To Clear The Order ?'):
    order.delete(*order.get_children())

#----------------------The End Of Clear Message-----------------------


#----------------------The Start Of Delete Function--------------------

def delete_row():
  v=order.selection() 
  for i in v:
    order.delete(i) 

#---------------------------------------------------------------------

window.title("Coffe Home") #The title of The window
resize_and_center(window,1300,600) #the resize function
window.resizable(False,False) #The resizable command 

#----------------------------------------------------------------------

#----------------The Menu Frame----------------
menu_frame=Frame(window,relief=FLAT)
menu_frame.pack(side='left')
#---------------The End Of Menu Frame----------

#----------------The Icons Of The Menu Frame Buttons------------
p1=PhotoImage(file='coffee.png')
p2=PhotoImage(file='drink.png')
p3=PhotoImage(file='ice.png')
p4=PhotoImage(file='logout.png')
#-----------------------The End Of Menu icons--------------------

#---------------The Logo icon-------------
icon=PhotoImage(file='coffee-cup.png')
window.iconphoto(TRUE,icon)
#-------------The End Of Logo icon--------


#--------The Starrt Of The left Frame Menus------------

#-------------The Getter of The on Value----------

x=StringVar()

#---------------The hot Dinks Button----------
Radiobutton(
    menu_frame,
    font=("Segoe Print",20),
    variable=x,
    value='Hot Drinks',
    image=p1,
    text='Hot Drinks',
    compound='top',
    padx=6,
    indicatoron=0,
    width=200,
    pady=20,
    command=lambda:show_drinks(x.get())
  ).pack()
#--------------------------------------------

#-----------------------------The cold_Drinks Button-----------------
Radiobutton(
    menu_frame,
    font=("Segoe Print",20),
    variable=x,
    value='Cold Drinks',
    image=p2,
    text='Cold Drinks',
    compound='top',
    padx=6,
    indicatoron=0,
    width=200,
    pady=20,
    command=lambda:show_drinks(x.get())
  ).pack()
#------------------------------------------------

#--------------------------The Ice Cream Button-------------------------
Radiobutton(
    menu_frame,
    font=("Segoe Print",20),
    variable=x,
    value='Sweets',
    image=p3,
    text='Sweets',
    compound='top',
    padx=6,
    indicatoron=0,
    width=200,
    pady=19,
    command=lambda:show_drinks(x.get())
  ).pack()
#---------------------------------------------------

#----------------------------The Exit Button-----------------------
Radiobutton(
    menu_frame,
    font=("Segoe Print",20),
    variable=x,
    value='exit',
    image=p4,
    text='Exit',
    compound='top',
    padx=6,
    indicatoron=0,
    width=200,
    pady=14,
    command=Exit
  ).pack(fill=BOTH)

#------------------------------------------------------

#---------------------The End Of The Left Menu Frame --------------------

#---------------Start of right side bar for calculating The Price -----------------

#----------------------------The Start Of The Right Frame---------------------------
right_frame=Frame(
  window,
  bg="#c9b98b",
  relief=FLAT
)
right_frame.pack(side='right',fill=BOTH)
yscroll=Scrollbar(right_frame,orient=VERTICAL)
yscroll.pack(side=RIGHT,fill=Y)
#------------------------------The End Of The right Frame----------------------------

#------------------start of treeview in right frame---------------------
order=ttk.Treeview(
  right_frame,
  yscrollcommand=yscroll.set
  )
yscroll.configure(command=order.yview)
order.configure(height=15)
#--------------------order Columns----------------------------
order['columns']=('Name','Quantity','Price')
#-------------------------------------------------------------

#-----------------------order columns_Declare-------------------
order.column('#0',width=0,stretch=NO)
order.column('Name',anchor=CENTER,width=165)
order.column('Quantity',anchor=CENTER,width=130)
order.column('Price',anchor=CENTER,width=130)
#----------------the End Of declare-----------------------------

#----------------The Stare Of order Headings--------------------
order.heading('Name',text='Name',anchor=CENTER,)
order.heading('Quantity',text='Quantity',anchor=CENTER)
order.heading('Price',text='Price',anchor=CENTER)
#----------------The End Of order Headings----------------------
order.pack(fill=BOTH)
#----------------End Of The TreeView----------------------------

#---------------------------------------------------------------

#----------------The Start Of The Total Price And The Label----------------

#---------------------Label right_Frame---------------------
total_label=Entry(
  right_frame,
  bd=2,
  relief=SUNKEN,
  font=("Consolas",19,'bold'),
  width=20,
  bg='white',
  fg='black',
)
total_label.pack(pady=10,anchor=CENTER)
total_label.configure(justify=CENTER)
total_label.insert(0,0.0)
#--------------------The End Of Right_Frame label------------

#--------------------The Total Button------------------------
Button(
  right_frame,
  font=('Consolas',13,'bold'),
  text='Total',
  width=18,
  pady=10,
  bg='#b0d4ca',
  fg='black',
  relief=GROOVE,
  command=lambda:total_price()
).pack()
#-------------------------------------------------------------

#----------------------The Confrim Button---------------------
Button(
  right_frame,
  font=('Consolas',13,'bold'),
  text='Confirm',
  padx=10,
  pady=20,
  command=confirm_window,
  bg='#b0d4ca',
  fg='black',
  relief=GROOVE
).pack(side=RIGHT,padx=15)
#-------------------------------------------------------------

#--------------------The Delete Button------------------------ 

Button(
  right_frame,
  font=('Consolas',13,'bold'),
  text='Delete',
  padx=10,
  pady=20,
  bg='#b0d4ca',
  fg='black',
  relief=GROOVE,
  command=lambda:delete_row()
).pack(side=LEFT,padx=20)

#-------------------------------------------------------------

#----------------------The End Of The right_Frame-------------------- 



#----------------------start of modify_frame------------------------
modify=Frame(
    window,
)
modify.pack(side=BOTTOM)
#-------------------------------------------------------------------

#-------------------The Modify Frame Button's Icons-----------------
c1=PhotoImage(file='plus.png')
c2=PhotoImage(file='minus.png')
c3=PhotoImage(file='cancel.png')
#-------------------The End Of This Icons---------------------------


#-------------------The Add Button---------------------
Radiobutton(
    modify,
    font=("Segoe Print",20),
    variable=x,
    value='Add',
    image=c1,
    text='Add',
    compound='bottom',
    padx=6,
    indicatoron=0,
    width=200,
    pady=15,
    command=lambda:add()
  ).grid(row=0,column=0)
#----------------------------------------------

#----------------------------The Remove Button------------------------
Radiobutton(
    modify,
    font=("Segoe Print",20),
    variable=x,
    value='Remove',
    image=c2,
    text='Remove',
    compound='bottom',
    padx=6,
    indicatoron=0,
    width=200,
    pady=15,
    command=remove
  ).grid(row=0,column=1)
#------------------------------------------------------------------------

#--------------------------The Clear Button------------------------------
Radiobutton(
    modify,
    font=("Segoe Print",20),
    variable=x,
    value='Clear',
    image=c3,
    text='Clear',
    compound='bottom',
    padx=6,
    indicatoron=0,
    width=200,
    pady=15,
    command=clear
  ).grid(row=0,column=2)
#--------------------------------------------------------------------------


#-------------------------The End Of Modify frame -------------------------

#-------------------------The Begin Of The Center Frame--------------------
center_frame=Frame(
  window,
  bg='black',
  bd=1,
  relief=SUNKEN
)
center_frame.pack(side=TOP)
#--------------------------------------------------------------------------

#-----------------------The Begin Of The Menu TreeView---------------------
yscroll=Scrollbar(center_frame,orient=VERTICAL)
yscroll.pack(side=RIGHT,fill=Y)
menu=ttk.Treeview(
  center_frame,
  yscrollcommand=yscroll.set
  )
menu.configure(height=100)
yscroll.configure(command=menu.yview)
#------------------------menu Columns---------------------------------------
menu['columns']=('ID','Name','Price','Category')
#----------------------------------------------------------------------------
#-------------------------------columns_Declare------------------------------
menu.column('#0',width=0,stretch=NO)
menu.column('ID',anchor=CENTER,width=50)
menu.column('Name',anchor=CENTER,width=200)
menu.column('Price',anchor=CENTER,width=200)
menu.column('Category',anchor=CENTER,width=200)
#----------------------------------The End Of Declare-------------------------

#----------------------------------menu Headings-----------------------------
menu.heading('ID',text='ID',anchor=CENTER,)
menu.heading('Name',text='Name',anchor=CENTER,)
menu.heading('Price',text='Price',anchor=CENTER)
menu.heading('Category',text='Category',anchor=CENTER)
#------------------------------------------------------------------------------

#---------------------------menu Excution-------------------------------------
menu.pack()
#---------------------------The End Of menu-----------------------------------

#-----------------------showing The Start Data------------------
def filter1(category,t1):
        t1.delete(*t1.get_children())
        data=connect_data.filter1(category)
        for item in data:
                t1.insert('',END, values=item)  
filter1('all',menu)
#-----------------------showing The Start Data------------------

#----------------------The End Of The Window--------------------------------------

window.mainloop()

#---------------------------------------------------------------------------------