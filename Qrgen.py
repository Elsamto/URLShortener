#pip import qrcode
#pip install image
import qrcode

data = input("Enter Data: ")

version=int(input("enter the version (complexity): ")) #maxvalue15
box_size=int(input("Enter the Box size")) #MAx10

qr = qrcode.QRCode(version, box_size, border= 5)

qr.add_data(data)

qr.make(fit= True)
img = qr.make_image(fill_color = "black", back_color="white")

f = input("name it as: ")

img.save(f"{f}.png")

print("qr generated and save in the gallery")