# QR-Code-Generator
You will learn how to create your own QR code and decode QR codes from an image by reading this repository. You should be able to include QR code capabilities into your own Python application at the conclusion of this. For this project, I'm utilising the python-qrcode package.

## Content
* [What is QR code?](#what-is-qr-code)
* [What information QR code takes?](#what-information-qr-code-takes)
* [Installation](#installation)
* [QR Code generator](#qr-code-generator)
  - [Generating Procedure](#generating-procedure)
  - [Python code for basic example](#python-code-for-basic-example)
  - [Advanced usage](#advanced-usage)
    - [Qr code class](#qr-code-class)
    - [Error Correction constant](#error-correction-constant)

## What is QR code?
A QR code is a type of barcode that can be read easily by a digital device and which stores information as a series of pixels in a square-shaped grid, which can be read by any imaging device such as a camera, and processed to extract the required data from the patterns that are present in the horizontal components of the image.

Standard barcodes can only be read in one direction – top to bottom. That means they can only store a small amount of information, usually in an alphanumeric format. But a QR code is read in two directions – top to bottom and right to left. This allows it to house significantly more data.

The data stored in a QR code can include website URLs, phone numbers, or up to 4,000 characters of text.

## What information QR code takes?
QR code-generating software does not collect personally identifiable information.

The data it does collect – and which is visible to the code’s creators – includes location, the number of times the code has been scanned and at what times, plus the operating system of the device which scanned the code (i.e., iPhone or Android).

The QR codes themselves can’t be hacked – the security risks associated with QR codes derive from the destination of QR codes rather than the codes themselves.

## Installation
```python
pip install qrcode
```
```python
pip instal opencv-Python
```
The package will be installed in the system as the version of Python and pip.

Once the installation is complete, create a new Python file and type the following syntax in it.
```python
# importing the required module  
import qrcode
```
```python
# importing the required module  
import cv2
```
# QR Code generator

## Generating Procedure
* Import module
* Create Qrcode with qrcode.make() and it returns a PilImage object.
* Save into image

## Python code for basic example
```python
import qrcode

# String which represent the QR code
qrcode_generator = "QR code Generator"

# Encoding data using make() function
img = qrcode.make(qrcode_generator)

# Create and save the image file by naming it
img.save("Create_qr_code.png")
```

## Advanced usage
You can utilize the QRCode class, which comes with a lot more controls and properties.

```python
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
```

In the above snippet of code, we have imported the qrcode library. We have then created an instance of the QRCode class of the qrcode library. We have used different parameters in order to customize the QR code. We have then used the add_data() function to include the information for the QR code. We have also used the make() and make_image() functions to generate the QR code image. At last, we have saved the image file in the directory using the save() function.

### QR code class
* **version** — Accepts an integer from 1 to 40 which controls the size of the QR Code. The smallest version 1 has a dimension of 21 x 21.

* **box_size** — Determines the number of pixels for each box of the QR code.

* **border** — Determines the thickness of the border of the boxes. The default value is 4, which is the minimum size.

* **error_correction** — Controls the error correction used.

### Error Correction constant
Error correction helps to improve the detection even when the image is disfigured or there is an overlay image on top of the QR Code. There are four constants available for error_correction:

* **ERROR_CORRECT_L** — About 7% or fewer errors can be corrected.

* **ERROR_CORRECT_M** — About 15% or fewer errors can be corrected. This is the default value.

* **ERROR_CORRECT_Q** — About 25% or fewer errors can be corrected.

* **ERROR_CORRECT_H** — About 30% or fewer errors can be corrected.

## Conclusion
A QR code is a matrix type 2D barcode (also known as checkerboard type 2D barcode), which has been frequently used on mobile devices in recent years. Compared with traditional barcodes, it can store more information. A two-dimensional code uses a certain geometric figure to record data symbol information in a black and white pattern distributed on a plane (two-dimensional direction) according to a certain rule. It can record numbers, English letters, Chinese characters, Japanese letters, special symbols (such as spaces, %, / etc.), binary information and other information into a square picture. In the position of the corresponding element of the matrix, the appearance of dots (square dots, dots or other shapes) is used to represent binary “1”, and the absence of dots represents binary “0”. The permutation and combination of points determine the meaning of the matrix two-dimensional bar code.
