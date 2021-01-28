from pyzbar import pyzbar
from cv2 import cv2

image = cv2.imread("qr3.png")
barcodes = pyzbar.decode(image)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type

    print("{} found : {}".format(barcodeType, barcodeData))
"""
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 2)
"""

cv2.imshow("Image", image)
cv2.waitKey(0)
