import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgtoText = pytesseract.image_to_string(img)
print(imgtoText)
cv2.imshow('Result Img', img)
cv2.waitKey(0)