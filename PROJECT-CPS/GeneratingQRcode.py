import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *


def getValue():
    x=fnValue.get()
    y=snValue.get()
    z=cnValue.get()
    op=x+'-'+y+'-'+z

    return op

def reset():
    fnValue.set('')
    snValue.set('')
    cnValue.set('')



#TK - Visualization ----------------------------------------------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.geometry('785x175')

root.title('CPS / 2021')
Label(root,text='   ').grid(row=1,column=4)
Label(root,bg='Light Blue',text=' <<  WELCOME TO CPS  >> ',font="Helvetica 18 bold").grid(row=2,column=4)
Label(root,text='   ').grid(row=3,column=4)
fn=Label(root,text='  Enter First Name    -  ')
sn=Label(root,text='  Enter Last Name    -  ')
cn=Label(root,text='  Enter Car Number  -  ')

fn.grid(row=4,column=2)
sn.grid(row=5,column=2)
cn.grid(row=6,column=2)

fnValue=StringVar()
snValue=StringVar()
cnValue=StringVar()

fnentry=Entry(root,bg='Orange',textvariable=fnValue)
snentry=Entry(root,textvariable=snValue)
cnentry=Entry(root,bg='Green',textvariable=cnValue)

fnentry.grid(row=4,column=3)
snentry.grid(row=5,column=3)
cnentry.grid(row=6,column=3)

b=Button(root,fg='Blue',bg='Pink',text='       SUBMIT DETAILS      ',command=getValue).grid(row=5,column=5)
b1=Button(root,fg='Black',bg='Red',text='   RESET   ',command=reset).grid(row=5,column=6)

root.mainloop()


# QRCODE Generation ----------------------------------------------------------------------------------------------------------------------------------------------------------------
s ='CPS-'+getValue()
qr = pyqrcode.create(s)

# Saving into -- "myqr.png" --------------------------------------------------------------------------------------------------------------------------------------------------------
qr.png('myqr.png', scale=10)

'''
@ ~ TSG405,2021
'''
