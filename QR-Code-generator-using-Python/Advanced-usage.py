import qrcode
# creating a QRCode object  
qr_object = qrcode.QRCode(  
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,  
    box_size = 10,  
    border = 4,  
)

# using the add_data() function  
qr_object.add_data("Advance use of QR code module") 

# using the make() function  
qr_object.make(fit = True)

# using the make_image() function  
qr_img = qr_object.make_image(fill_color = "red", back_color = "black")  

# saving the QR code image  
qr_img.save("advancedusage.png")
