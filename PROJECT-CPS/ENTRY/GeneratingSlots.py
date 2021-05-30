def GivingSlots(SlotList,NumberOfVacantSlots):
    
    fh = open('QRcode_result.txt')                                                                 # Accessing QR-Response Text!
    for i in fh:
        l = i.split('-')
    carNumber = l[-3]
    fh.close()

    # Slot Registration ------------------------------------------------------------------------------------------------------------------------------------------------------------
    if NumberOfVacantSlots >= 1:
        for j in range(len(SlotList)):

            if SlotList[j] == 'null':
                SlotList[j] = carNumber
                print("\n\n-------------------------------------------------------")
                print('Your Slot Number is ---', j+1)
                print("-------------------------------------------------------\n\n")
                break
    else:
        print('SORRY! Currently No Slot is Available!!!')
    
    return (SlotList)

# Driver Code ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    GivingSlots([],50)
    
 
'''
@ ~ TSG405,2021
'''
