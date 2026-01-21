import qrcode  
from PIL import Image


upi_id = input("Enter your UPI ID = ")
amount = input("Enter Amount = ")
name = input("Enter your Name = ")

if not upi_id or not amount or not name:
    print("All fields are required")
    exit()

if not amount.isdigit():
    print("Enter a valid number for amount")
    exit()

upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

qr.add_data(upi_url)
qr.make(fit=True)

upi_qr = qr.make_image(fill_color="green", back_color="white")
    
qr_img = upi_qr.convert("RGBA")

logo = Image.open("logo.png").convert("RGBA")

qr_width, qr_height = qr_img.size
logo_size = qr_width//6

logo = logo.resize((logo_size, logo_size))

pos = (
    (qr_width - logo_size) // 2,
    (qr_height - logo_size) // 2
)

qr_img.paste(logo, pos, mask=logo)

qr_img.save("example_qr.png")
qr_img.show()