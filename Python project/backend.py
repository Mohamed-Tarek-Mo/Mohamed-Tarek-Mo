from tkinter import messagebox
from tkinter import * 
from tkinter import ttk
import Database as db
GUI_DB=Tk()
GUI_DB.title('Management')
GUI_DB.resizable(FALSE,FALSE)
#GUI_DB.geometry('1300x600')
icon=PhotoImage(file='coffee-cup.png')
GUI_DB.iconphoto(TRUE,icon)


#----------------------Style Trees------------
style=ttk.Style()
style.theme_use('clam')
style.configure(
  "Treeview",
  background='silver',
  foreground='black',
  rowheight=20,
  fieldbackground='silver'
)
style.map(
  "Treeview",
  background=[('selected','green')]
)
#-------------------------

#   Functions
# -------------
def openmnue():
    GUI_DB.destroy()
    from gui import window
    
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
resize_and_center(GUI_DB,1300,600)


# begin of Icons

c1=PhotoImage(file='plus.png')
c2=PhotoImage(file='menu.png')
c3=PhotoImage(file='update.png')
c4=PhotoImage(file='cancel.png')
logo=PhotoImage(file='coffee-shop.png')

#end Of Icons

#------------------------------
# Create main_frame (container)
main_frame=Frame(GUI_DB,bg='black')
main_frame.pack(fill=BOTH,expand=True)
#---------------------------------------

# Create The Top frame
top_frame=Frame(main_frame,bg='#0b99b3')
top_frame.pack(side=TOP,anchor=W)
# ---------------------------------------

# 1-create top left frame (Getting data)
getdata_frame=Frame(top_frame,bg='#0b99b3')
getdata_frame.pack(side='left',anchor='se')
#-----------------------------------------


#-------------Label For The Data Management-------------

top_label=Label(
  top_frame,
  text='Data Management',
  image=logo,
  compound='top',
  font=("Segoe Print",20),
  fg='black',
  bg='#0b99b3'
)
top_label.place(x=80,y=110,anchor=W)

#----------The End Of The Top Label--------------- 
# creat labels
name_label=Label(getdata_frame,text='Name',relief=RIDGE,font=("Segoe Print",14),width=10,height=1)
name_label.grid(row=0,column=0,padx=20,pady=10)
price_label=Label(getdata_frame,text='Price',width=10,height=1,font=("Segoe Print",14),relief=RIDGE)
price_label.grid(row=1,column=0,padx=20,pady=10)
category_label=Label(getdata_frame,text='Category',width=10,height=1,font=("Segoe Print",14),relief=RIDGE)
category_label.grid(row=2,column=0,padx=20,pady=10)
#---------------------------------------------------------------------------------
# Create Entries and menubar
name_entry=Entry(getdata_frame,width=20,font=("Consolas",15,'bold'),relief=RIDGE,bd=2)
name_entry.grid(row=0,column=1,padx=20, pady=10)
#-------------------------------------------------
price_entry=Entry(getdata_frame,width=20,font=("Consolas",15,'bold'),relief=RIDGE,bd=2)
price_entry.grid(row=1,column=1,padx=20, pady=10)
# --------------------------------------------------------------------------------
options=['Hot_Drinks','Ice_Drinks','Ice_Cream'] # List Of Options
# Create Of The Combo_options
clicked=StringVar()   # return value from option_combo
category_menu=ttk.Combobox(getdata_frame,value=options,textvariable=clicked,width=22,height=50)
category_menu.current(0)
category_menu.bind("<<ComboboxSelected>>",clicked)
category_menu.config(font=("Consolas",13,'bold'),state='readonly')
category_menu.grid(row=2,column=1,padx=20, pady=10)


# 2-create top right frame (treeview)
showdata_frame=Frame(top_frame)
showdata_frame.pack(side=RIGHT)
#--------------------------------------------------------------------------

# Treeeveiw
scroll_y=Scrollbar(showdata_frame,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)
show_tree=ttk.Treeview(
        showdata_frame,
        columns=('ID','Name','Price','Category'),
        height=24,
        yscrollcommand=scroll_y.set,
        )
scroll_y.configure(command=show_tree.yview)
# --------------------------------------------------



#---------------------------------------------------

#-----------------------Create Of Columns-------------------
show_tree.column('#0',width=0,stretch=NO)
show_tree.column('ID',anchor=CENTER,width=60)
show_tree.column('Name',anchor=CENTER,width=280)
show_tree.column('Price',anchor=CENTER,width=260)
show_tree.column('Category',anchor=CENTER,width=270)
# ----------------------End Of Columns------------------------

#---------------Headings-------------------------
show_tree.heading('ID',text='ID',anchor=CENTER,)
show_tree.heading('Name',text='Name',anchor=CENTER,)
show_tree.heading('Price',text='Price',anchor=CENTER)
show_tree.heading('Category',text='Category',anchor=CENTER)
#---------------End Of Headings-------------------
show_tree.pack()
###################   Functions  ########################
# ----------->filteration
def filter(category,t1):
        t1.delete(*t1.get_children())
        data=db.show_items(category)
        for item in data:
                t1.insert('',END, values=item)
filter('All',show_tree)                             
# -------------------
def clear_data(n,p,c):
        n.delete(0,END)
        p.delete(0,END)
        c.delete(0,END)
# ---------------->add_button
def add_button():
        try:    
                name=name_entry.get()
                price=price_entry.get()
                category=clicked.get()
                if name.isnumeric() or price ==''or name=='':
                        messagebox.showerror(title='Type Error',message='Enter correct Data')
                        return
                if len(name)>0 and price and category :
                        name=str(name)                
                        price=float(price)
                        if db.check_name_exist(name):
                                messagebox.showerror(title='Type Error',message='This data already exist')
                                return
                db.add_item(name,price,category)
                filter('All',show_tree)         
                
                        
        except:
                messagebox.showerror(title='Type Error',message='Invalid Input')
        finally:
                clear_data(name_entry,price_entry)
        # meun_treeview Excution

# ---------End Of The Excution---------
#--------------------------------------------------------------------------
# Add Button
addbuttton=Button(
        getdata_frame,
        text='Add',
        font=("Segoe Print",15,'bold'),
        image=c1,
        compound='left',
        padx=30,
        pady=10,
        command= add_button
        )
addbuttton.grid(row=3,column=0,columnspan=2,rowspan=2,pady=20,padx=20)
# -------------------------------------------------------------------------


#-------------Buttom Frame-------------------------
buttons_frame=Frame(main_frame)
buttons_frame.pack(side=BOTTOM,expand=True,fill=BOTH)
#------------End Of Buttons Frame------------------

# ---------------Delete Button---------------------

def delete_button():
    from Database import Delete_item
    v=show_tree.item(show_tree.focus())['values']
    
    Delete_item(v[0])
    show_tree.delete(*show_tree.selection())
    messagebox.showwarning(title='show deleted',message='Record Has Been Deleted')    
deletebutton=Button(
        buttons_frame,
        text='Delete',
        font=("Segoe Print",15,'bold'),
        image=c4,
        compound='left',
        padx=20,
        command=delete_button
        )
deletebutton.pack(side=RIGHT,expand=True,fill=BOTH)

#--------End Of delete Button-------------

# ----------------Update Button---------------------

def update():
        
        try:    
                name=name_entry.get()
                price=price_entry.get()
                category=clicked.get()
                if len(name)>0 and price and category :
                        name=str(name)                
                        price=float(price)
                        if db.check_name_exist(name,price):
                                 messagebox.showerror(title='Type Error',message='This data exist')                       
                        else:
                                v=show_tree.item(show_tree.focus())['values']
                                db.update_item(name,price,category,v[0])
                                row=show_tree.selection()[0]
                                show_tree.item(row,text='',values=(
                                        name,
                                        price,
                                        category
                                ))
                                filter('All',show_tree)
        except:
                messagebox.showerror(title='Type Error',message='Invalid Input')
        finally:
                clear_data(name_entry,price_entry)
        


updatebutton=Button(
        buttons_frame,
        text='Update',
        font=("Segoe Print",15,'bold'),
        image=c3,
        compound='left',
        padx=20,
        command=update
        )
updatebutton.pack(side=RIGHT,expand=True,fill=BOTH)
#---------End Of Update Button----------------------

#----------------Menu Button----------------------
goto_screen_cashierbutton=Button(
        buttons_frame,
        text='Menu/Login',
        #command=openmnue,
        font=("Segoe Print",15,'bold'),
        image=c2,
        compound='left',
        bd=2,
        padx=81.5,
        pady=10,
        relief=FLAT,
        bg='black',
        fg='white',
        )
goto_screen_cashierbutton.pack(side=RIGHT,fill=BOTH)

def Go_Back(event):
    GUI_DB.destroy()
    import Login
def Go_Menu(event):
    GUI_DB.destroy()
    import gui

goto_screen_cashierbutton.bind('<Button-1>',Go_Back)
goto_screen_cashierbutton.bind('<Button-3>',Go_Menu)
#---------------------------------------------------------------


#--------------End Of Menu Button------------------

GUI_DB.mainloop()