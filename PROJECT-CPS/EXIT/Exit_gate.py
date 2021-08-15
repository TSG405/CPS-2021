import math
import sqlite3
import ScanningTheCode
from datetime import datetime
from gtts import  gTTS
import os

ScanningTheCode.main()                                                                       # This function will scan the Qrcode and send the data into database. Press 'q' to exit!
fh=open('QRcode_result.txt')                                                                 # Accessing QR-Response Text!

  
# Opening scanned File -----------------------------------------------------------------------------------------------------------------
fh = open('QRcode_result.txt')

for i in fh:

    l = i.split(':')

    if l[-1].startswith('CPS'):
        WorkingList = l[-1].split('-')

        # Collecting Values -------------------------------------------------------------------------------------------------------------
        cn = WorkingList[3]

        # Connecting to Database Server -------------------------------------------------------------------------------------------------
        conn = sqlite3.connect("CPS.sqlite")

        cur = conn.cursor()
        row = cur.fetchone()

        now = datetime.now()
        date,Exit_time = now.strftime("%d/%m/%Y %H:%M:%S").split(' ')

        # Registering into Database -----------------------------------------------------------------------------------------------------
        if row is None:
            try:
                cur.execute('''UPDATE CPSDATABASE SET EXIT_TIME = "{0}" WHERE CAR_NUMBER = "{1}";'''.format(Exit_time, cn))
                cur.execute('''SELECT ENTRY_TIME FROM CPSDATABASE WHERE CAR_NUMBER = "{0}";'''.format(cn))
                for row in cur.fetchall():
                    Entry_time = row[0]
                conn.commit()

                l2 = Entry_time.split(":")
                l1 = Exit_time.split(":")

                h = int(l1[0]) - int(l2[0])
                m = abs(int(l1[1]) - int(l2[1]))
                s = abs(int(l1[2]) - int(l2[2]))

                total_time_taken = (h*60 + m + s/60)
                Need_to_pay=int(total_time_taken*(10/60))

                # Registering the Amount into Database --------------------------------------------------------------------------------------------------------------------------------------------
                conn = sqlite3.connect("CPS.sqlite")
                cur = conn.cursor()
                row = cur.fetchone()

                if row is None:
                    try:
                        cur.execute('''UPDATE CPSDATABASE SET AMOUNT = {0} WHERE CAR_NUMBER = "{1}";'''.format(Need_to_pay, cn))
                        conn.commit()
                    except:
                        print('ERROR! QUERYING DATABASE!!')   


                # DISPLAY ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                print("\n\n-------------------------------------------------------")
                print("CPS Parking Charge: ₹10/hr only!")
                print("-------------------------------------------------------")

                print(("\nYou reserved {} minutes..... \nYou Need To Pay Rs: {}/- only!").format(total_time_taken,Need_to_pay))

                print("\n-------------------------------------------------------")
                print("Thank You! Do Visit Again!")
                print("-------------------------------------------------------\n\n")

                # Accessing DatabaseList ------------------------------------------------------------------------------------------------------------------------------------------------------------
                ss=open('SLOTLIST.txt','r')
                SlotList=[]
                for i in ss:
                    SlotList += i.split(' ')
                ss.close()
                SlotList.remove(SlotList[-1])

                j = SlotList.index(cn)
                SlotList[j] = "null"

                # Updating DatabaseList -----------------------------------------------------------------------------------------------------------------------------------------------------
                u = open('SLOTLIST.txt',"w")
                for hh in SlotList:
                    u.write(hh+" ")
                u.close()

                # Payment clearance and voice O/P -------------------------------------------------------------------------------------------------------------------------------------------
                kk = input("Press 'Y' or 'y' after successful Payment: \t").lower()
                
                if kk =="y":
                    s="You paid "+str(Need_to_pay)+"rupees to us. Thank You! Do Visit Again!"
                    ob=gTTS(text=s,lang='en',slow=False)
                    ob.save("t.mp3")
                    os.system("start t.mp3")
            
            except:
                print('ERROR! QUERYING DATABASE (Hint: Check Car Number)!!')    
        else:
            print('SORRY! Not Our QRcode!!')
            
            
'''
@ ~ TSG405,2021
'''
