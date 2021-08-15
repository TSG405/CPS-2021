from pyzbar import pyzbar
import cv2


def read_qrcode(frame,l):
    qrcodes = pyzbar.decode(frame)
    
    for code in qrcodes:
        x, y, w, h = code.rect

        # Creating Framework
        qrcode_info = code.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display Scanned QR Text (Immediate Response!)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, qrcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        # Converting and saving the response in a text file -- 'QRcode_result.txt'
        with open("QRcode_result.txt", mode='w') as file:
            file.write("Recognized QRode:" + qrcode_info)
        
        l.append(qrcode_info)
        print(qrcode_info)

    return frame,l


# Driver Code -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    l=[]
    while ret:
        ret, frame = camera.read()
        frame,l = read_qrcode(frame,l)
        cv2.imshow('QR code reader', frame)

        if cv2.waitKey(1) & len(l)>0:
            break

    camera.release()
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()
    
    
'''
@ ~ TSG405,2021
'''
