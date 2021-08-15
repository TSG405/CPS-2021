import sqlite3
from tkinter import *
import hashlib    


root=Tk()
root.geometry('560x425')
root.title('CPS QUERY SYSTEM')


# Button Function (1) ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit():
    entered_car_number=car_number.get()
    
    conn = sqlite3.connect("CPS.sqlite")
    cur = conn.cursor()
  
    # Querying Database -------------------------------------------------------------------------------------------------------------------------------------------------------------
    cur.execute('''SELECT FIRST_NAME,LAST_NAME,PH_NO FROM CPSDATABASE WHERE CAR_NUMBER="{0}";'''.format(entered_car_number))
    for row in cur.fetchall():
        Your_name.set(row[0]+ ' ' +row[1])
        contact_number.set(row[2])
    
    conn.commit()


# Button Function (2) ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit1():
    entered_phno=contact_number.get()
    entered_car_number=car_number.get()
    password = entered_password.get()
    orgpwd=''
    
    kk = hashlib.md5(password.encode()).hexdigest()                # Hashing pwd via MD5 Algorithm

    conn = sqlite3.connect("CPS.sqlite")
    cur = conn.cursor()

    # Querying Database -------------------------------------------------------------------------------------------------------------------------------------------------------------
    cur.execute('''SELECT PWD FROM CPSDATABASE WHERE PH_NO="{0}"'''.format(entered_phno))
    for row1 in cur.fetchall():
        orgpwd=row1[0]

    conn.commit()

    # Querying DatabaseList ---------------------------------------------------------------------------------------------------------------------------------------------------------
    ss=open('SLOTLIST.txt','r')
    SlotList=[]
    for i in ss:
        SlotList += i.split(' ')
    ss.close()
    SlotList.remove(SlotList[-1]) 

    # PWD Validation ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if kk==orgpwd:
        status.set("         MATCHED !")

        # SLOT Display ------------------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            slot.set(SlotList.index(entered_car_number)+1)
        except:
            slot.set("        NO CAR found!")      
    else:
        status.set("    INCORRECT PWD!")

    
# FRAME 1 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame=Frame(root,bd=5,relief=RIDGE,bg="light Green")
frame.place(x=30,y=10,height=100,width=500)
Label(frame,text='QUERY',font="Helvetica 18 bold",bg="light Green").grid(row=0,column=1)
Label(frame,text='  Enter Car Number   ',font="Helvetica 14 bold",bg="light Green").grid(row=1,column=0)
Label(frame,text='       ',bg="light Green").grid(row=1,column=3)
car_number=StringVar()
Entry(frame,textvariable=car_number).grid(row=1,column=1)
Button(frame,text='           SUBMIT          ',bg="Yellow",command=submit).grid(row=1,column=4)


# FRAME 2 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame1=Frame(root,bd=5,relief=RIDGE,bg="pink")
frame1.place(x=100,y=125,height=100,width=385)
Label(frame1,text='DETAILS',font="Helvetica 16 bold",bg="pink").grid(row=0,column=1)
Label(frame1,text='  Name  ',font="Helvetica 10 bold",bg="pink").grid(row=2,column=0)
Label(frame1,text='  Phone Number  ',font="Helvetica 10 bold",bg="pink").grid(row=3,column=0)
Label(frame1,text='       ',bg="Pink").grid(row=3,column=3)
Your_name=StringVar()
contact_number=IntVar()
Entry(frame1,textvariable=Your_name).grid(row=2,column=4)
Entry(frame1,textvariable=contact_number).grid(row=3,column=4)


# FRAME 3 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame2=Frame(root,bd=5,relief=RIDGE,bg="Light Blue")
frame2.place(x=160,y=250,height=160,width=275)
Label(frame2,text='   ',bg="Light Blue").grid(row=0,column=1)
Label(frame2,text='   ',bg="Light Blue").grid(row=4,column=1)
Label(frame2,text='  Enter Password  ',font="Helvetica 10 bold",bg='Light Blue').grid(row=2,column=0)
Label(frame2,text='  Status  ',font="Helvetica 10 bold",bg='Light Blue').grid(row=5,column=0)
Label(frame2,text='  Slot  ',font="Helvetica 10 bold",bg='Light Blue').grid(row=6,column=0)
entered_password=StringVar()
status=StringVar()
slot=IntVar()
Entry(frame2,textvariable=entered_password).grid(row=2,column=1)
Entry(frame2,textvariable=status).grid(row=5,column=1)
Entry(frame2,textvariable=slot).grid(row=6,column=1)
Button(frame2,text='VALIDATE',bg="Yellow",command=submit1).grid(row=3,column=1)

root.mainloop()


'''
@ ~ TSG405,2021
'''
