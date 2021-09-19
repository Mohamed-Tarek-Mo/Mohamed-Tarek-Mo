
import sqlite3

DB_name='database.db'
# ADD FUNCTION
def add_item(name,price,category):
    conn=sqlite3.connect(DB_name)
    conn.execute(
        '''
        insert into menu(d_name,d_price,d_category) 
        values(?,?,?)
        ''',(name,price,category)
    )
    conn.commit()
    conn.close()
    
# UPDATE FUNCTION
def update_item(name,price,category,id):
    conn=sqlite3.connect(DB_name)
    conn.execute(
        '''update menu set d_name=?,d_price=?,d_category=? where menu_id=?'''
        ,(name,price,category,id)
    )
    conn.commit()
    conn.close()
update_item('Strawberry Smoothie',20,'Ice_Cream',14)

# DELETE FUNCTION
def Delete_item(id):
    conn=sqlite3.connect(DB_name)
    conn.execute(
        '''delete from menu where  menu_id=?''',(id,)
    )
    conn.commit()
    conn.close()
    



# SHOW ALL DATA FUNCTION
def show_items(category):
    conn=sqlite3.connect(DB_name)
    filter=conn.execute(
        '''select * from menu''')
    date=list(filter)
    hot=[]
    cold=[]
    ice=[]
    for i in range(len(date)):
            if date[i][3]=='Hot_Drinks':
                hot.append(date[i])
            elif date[i][3]=='Ice_Drinks':
                cold.append(date[i])
            elif date[i][3]=='Ice_Cream':
                ice.append(date[i])
    conn.commit()
    conn.close()
    if  category=='Hot Drinks':
        return hot
    elif  category=='Ice Drinks':
        return cold
    elif  category=='Ice Cream':
        return ice
    else:
        return date

# delete Repeated value
def delete_repepted():
    name=dict()
    data=list(show_items('all'))
    for i in data:
        name[i[1]]=name.get(i[1],0)+1
        for value in name.values():
            if value>1:
                Delete_item(i[0])
# check if name exist or not
def check_name_exist(name,price):
    conn=sqlite3.connect(DB_name)
    filter=conn.execute('''select * from menu where d_name=? and d_price=?''',(name,price))
    date=list(filter)
    conn.close()
    if len(date)>0 :
        return True
    else:
        return False
