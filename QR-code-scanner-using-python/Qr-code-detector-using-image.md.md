# QR-code-scanner
In this repository I have explained how to make qr code scanner using python module opencv and pyzbar.

OpenCV does not have any dedicated modules that can be used to read and decode barcodes and QR codes.However, what OpenCV can do is facilitate the process of reading barcodes and QR codes, including loading an image from disk, grabbing a new frame from a video stream, and processing it.

Once we have the image or frame we can then pass it to a dedicated Python barcode decoding library such as a pyzbar.The pyzar library will then decode the barcode or QR code. OpenCV can come back in to perform any further processing and display the result.

## Installation
Install the required libraries using the following commands.

```python
pip install opencv
```

The official version of ZBar does not support Python 3. So I recommend using pyzbar which supports both python 2 and Python 3. If you just want to work with python 2, you can install zbar and skip installing pyzbar.

```python
pip install pyzbar
```

## Understanding the structure of QR code
A QR code object returned by pyzar has three fields

* **Type**: If the symbol detected by pyzar is a QR code, the type is QR-Code.
* **Data**: This is the data embedded inside the QR code. This data is usually alphanumeric, but other types ( numeric, byte/binary etc. ) are also valid.
* **Location**: This is a collection of points that locate the code. For QR codes, it is a list of four points corresponding to the four corners of the QR code quad.

## Python Code
**Decode QR Code Using QR Code Image**
```python
import cv2
qr_img = cv2.imread("/content/Create_qr_code.png")

# using the QRCodeDetector() function detect the qr code  
qr_det = cv2.QRCodeDetector()

# using the detectAndDecode() function  
val, pts, st_code = qr_det.detectAndDecode(qr_img)

# printing the value  print(val)
print(val)
```
**Decode QR Code Live Using a Webcam**
```python
import cv2

# initalize the camera
cap = cv2.VideoCapture(0)

# initialize the OpenCV QRCode detector
detector = cv2.QRCodeDetector()

while True:
  _, img = cap.read()

  # detect and decode
  data, vertices_array, _ = detector.detectAndDecode(img)

  # check if there is a QRCode in the image
  if vertices_array is not None:
    if data:
      print("QR Code detected, data:", data)

  # display the result
  cv2.imshow("img", img)

  # Enter q to Quit
  if cv2.waitKey(1) == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()
```
When you execute this code, your webcam will be automatically opened. Simply hold the QR code in front of the webcam and the data will be decoded and displayed in the command prompt.

## Conclusion
There are many tools that read QR codes. However, I used OpenCV for this, as it is popular and easy to integrate with the webcam or any video. You can even create a complete QR code Scanner-Generator application using the code provided.

Finally, many of the Python concepts aren't discussed in detail here, if you feel you want to dig more into Python.
