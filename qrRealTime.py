from pyzbar import pyzbar
from cv2 import cv2
import numpy as np

arrBarcode = list()
lastFrames = list()
cap = cv2.VideoCapture(0)
#  cap = cv2.VideoCapture(2)
width = 540
height = 960
dim = (width, height)

while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        lastFrames.append(frame)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        arrBarcode.append((barcodeType, barcodeData))

    cv2.imshow("Barcode Scanner", frame)
    cv2.imshow("Barcode Scanner 1", gray)
    key = cv2.waitKey(1)
    if len(arrBarcode) != 0 or key == ord("q"):
        cap.release()
        break
"""
for j in arrBarcode:
    print("{} : {}".format(j[0], j[1]))
for k in range(0, len(lastFrames)):
    cv2.imshow("Barcode Frame {}".format(k), lastFrames[k])
"""
print("{} : {}".format(arrBarcode[0][0], arrBarcode[0][1]))
cv2.imshow("Barcode Frame", lastFrames[0])
key = cv2.waitKey(0)
if key == ord("q"):
    cv2.destroyAllWindows()
    exit()
