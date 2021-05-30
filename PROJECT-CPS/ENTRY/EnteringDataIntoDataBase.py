import sqlite3
from datetime import datetime


def databaseEntry():
    # Opening scanned File -----------------------------------------------------------------------------------------------------------------
    fh = open('QRcode_result.txt')

    for i in fh:
        l = i.split(':')

        if l[-1].startswith('CPS'):
            WorkingList = l[-1].split('-')

            # Collecting Values -------------------------------------------------------------------------------------------------------------
            fn = WorkingList[1]
            ln = WorkingList[2]
            cn = WorkingList[3]
            pwd = WorkingList[4]
            ph = WorkingList[5]

            # Connecting to Database Server -------------------------------------------------------------------------------------------------
            conn = sqlite3.connect("CPS.sqlite")

            cur = conn.cursor()
            row = cur.fetchone()

            now = datetime.now()
            date,time = now.strftime("%d/%m/%Y %H:%M:%S").split(' ')
            etime ='NULL'
            # Registering into Database -----------------------------------------------------------------------------------------------------
            if row is None:
                try:
                    cur.execute('''INSERT INTO CPSDATABASE VALUES(?,?,?,?,?,?,?,?)''', (fn, ln, cn, date, time, etime, pwd, ph))
                except:
                    pass
            conn.commit()

        else:
            print('SORRY! Not Our QRcode!!')


# Driver Code ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    databaseEntry()
    
'''
@ ~ TSG405,2021
'''
