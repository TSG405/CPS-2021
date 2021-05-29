import ScanningTheCode
import EnteringDataIntoDataBase
import GeneratingSlots


# Accessing DatabaseList ------------------------------------------------------------------------------------------------------------------------------------------------------------
ss=open('SLOTLIST.txt','r')
SlotList=[]
for i in ss:
    SlotList += i.split(' ')
ss.close()
SlotList.remove(SlotList[-1])


# Displaying vacant slots -----------------------------------------------------------------------------------------------------------------------------------------------------------
NumberOfVacantSlots = SlotList.count('null')
print("-------------------------------------------------------")
print("Currently, Number Of Slots Available is :", NumberOfVacantSlots)
print("-------------------------------------------------------")

ScanningTheCode.main()                                                                       # This function will scan the Qrcode and send the data into database. Press 'q' to exit!
fh=open('QRcode_result.txt')                                                                 # Accessing QR-Response Text!

for i in fh: 
    l=i.split(':')

    # Data-Validation ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    if l[-1].startswith('CPS'):

        EnteringDataIntoDataBase.databaseEntry()                                             # This function will register the data into database!
        Slotlist = GeneratingSlots.GivingSlots(SlotList,NumberOfVacantSlots)                 # This function will generate slots for the Client!
        
        # Updating DatabaseList -----------------------------------------------------------------------------------------------------------------------------------------------------
        u = open('SLOTLIST.txt',"w")
        for h in SlotList:
            u.write(h+" ")
        u.close()
        
    else:
        print("Sorry this is not our QRcode!!")


    # Displaying vacant slots -------------------------------------------------------------------------------------------------------------------------------------------------------
    print("-------------------------------------------------------")
    print("Currently Number Of Slots Available is :",SlotList.count('null'))
    print("-------------------------------------------------------")

    break
    
    
'''
@ ~ TSG405,2021
'''
