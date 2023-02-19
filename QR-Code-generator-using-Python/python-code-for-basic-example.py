import qrcode

# String which represent the QR code
qrcode_generator = "QR code Generator"

# Encoding data using make() function
img = qrcode.make(qrcode_generator)

# Create and save the image file by naming it
img.save("Create_qr_code.png")
