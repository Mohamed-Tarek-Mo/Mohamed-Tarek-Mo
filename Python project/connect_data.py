import sqlite3

def filter2(kind):  
    db=sqlite3.connect('database.db')
    cr=db.cursor()
    f=list(cr.execute("select * from menu"))
    hot=[]
    cold=[]
    ice=[]
    for i in range(len(f)):
        if f[i][3]=='Hot_Drinks':
            hot.append(f[i])
        elif f[i][3]=='Ice_Drinks':
            cold.append(f[i])
        elif f[i][3]=='Ice_Cream':
            ice.append(f[i])
    db.commit()
    db.close()
    if  kind=='Hot Drinks':
        return hot
    elif  kind=='Cold Drinks':
        return cold
    else:
        return ice
    
    

    
def filter1(kind):  
    db=sqlite3.connect('database.db')
    cr=db.cursor()
    f=list(cr.execute("select * from menu"))
    hot=[]
    cold=[]
    ice=[]
    for i in range(len(f)):
        if f[i][3]=='Hot_Drinks':
            hot.append(f[i])
        elif f[i][3]=='Ice_Drinks':
            cold.append(f[i])
        elif f[i][3]=='Ice_Cream':
            ice.append(f[i])
    db.commit()
    db.close()
    if  kind=='Hot Drinks':
        return hot
    elif  kind=='Cold Drinks':
        return cold
    elif kind=='Ice_Cream':
        return ice
    else:
        return f
    