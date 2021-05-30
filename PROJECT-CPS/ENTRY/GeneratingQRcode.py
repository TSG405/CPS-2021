import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
import hashlib                                                                          # For Enhanced Security Hashing (MD5)


def getValue():
    x=fnValue.get()
    y=snValue.get()
    z=cnValue.get()
    r=pwdValue.get()
    e=phValue.get()
    op=x+'-'+y+'-'+z+'-'+hashlib.md5(r.encode()).hexdigest()+'-'+str(e)
    stValue.set('            SUCCESS!   ')
    return op

def reset():
    fnValue.set('')
    snValue.set('')
    cnValue.set('')
    pwdValue.set('')
    phValue.set('')
    stValue.set('')


#TK - Visualization ----------------------------------------------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.geometry('785x250')
root.title('CPS / 2021')

Label(root,text='   ').grid(row=1,column=4)
Label(root,bg='Light Blue',text=' <<  WELCOME TO CPS  >> ',font="Helvetica 18 bold").grid(row=2,column=4)
Label(root,text='   ').grid(row=3,column=4)
fn=Label(root,text='  Enter First Name    -  ')
sn=Label(root,text='  Enter Last Name    -  ')
cn=Label(root,text='  Enter Car Number  -  ')
pwd=Label(root,text='  Enter Password  -  ')
ph=Label(root,text='  Enter Phone no.  -  ')

fn.grid(row=4,column=2)
sn.grid(row=5,column=2)
cn.grid(row=6,column=2)
pwd.grid(row=7,column=2)
ph.grid(row=8,column=2)


fnValue=StringVar()
snValue=StringVar()
cnValue=StringVar()
pwdValue=StringVar()
phValue=IntVar()
stValue=StringVar()

fnentry=Entry(root,bg='Orange',textvariable=fnValue)
snentry=Entry(root,textvariable=snValue)
cnentry=Entry(root,bg='Green',textvariable=cnValue)
pwdentry=Entry(root,bg='Yellow',textvariable=pwdValue)
phentry=Entry(root,textvariable=phValue)
stentry=Entry(root,bg='Light Blue',textvariable=stValue)

fnentry.grid(row=4,column=3)
snentry.grid(row=5,column=3)
cnentry.grid(row=6,column=3)
pwdentry.grid(row=7,column=3)
phentry.grid(row=8,column=3)
stentry.grid(row=9,column=4)

b=Button(root,fg='Blue',bg='Pink',text='       SUBMIT DETAILS      ',command=getValue).grid(row=6,column=5)
b1=Button(root,fg='Black',bg='Red',text='   RESET   ',command=reset).grid(row=6,column=6)

root.mainloop()


# QRCODE Generation ----------------------------------------------------------------------------------------------------------------------------------------------------------------
s ='CPS-'+getValue()
qr = pyqrcode.create(s)

# Saving into -- "myqr.png" --------------------------------------------------------------------------------------------------------------------------------------------------------
qr.png('myqr.png', scale=10)


'''
@ ~ TSG405,2021
'''
