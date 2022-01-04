#Importing Module for qr code
import qrcode
#Importing Module for Image Format
import image
#Importing Modules for Barcode
from barcode import EAN13
from barcode.writer import ImageWriter


#QR Code Generator
def qr(url):
    qr = qrcode.QRCode(
        version = 1,
        box_size = 15,
        border = 10
        )
    data = url
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "red", back_color = "white")
    img.save('Custom.png')
    

#Barcode Generator
def barcode(number):
    my_code = EAN13(number, writer=ImageWriter())
    my_code.save("bar_code.jpeg")
    

#Asking for the choice from the User
print("1 - QR Code Generator")
print("2 - Barcode Generator\n")
choice = int(input("Enter the Choice :"))


#Selecting the generator according to the choice
if (choice == 1):
    print("QR Code Generator :")
    url = input("Enter the URL :")
    qr(url)
elif(choice == 2):
    print("Barcode Generator :")
    number = input("Enter the Number :")
    barcode(number)
                   
