import cv2
import pytesseract
import pyttsx3
def speak(inpText):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(inpText)
    engine.runAndWait()

# Set the path to the Tesseract executable (change accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open a connection to the webcam (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for better OCR results
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale frame
    # text = pytesseract.image_to_string(gray)

    # hImg, wImg = frame.shape 
    # boxes = pytesseract.image_to_boxes(frame)
    # for b in boxes.splitlines():
    #     b = b.split(' ')
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(frame, (x,hImg-y), (w,hImg-h), (0, 0, 255), 1)

    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = pytesseract.image_to_string(gray, config=custom_config)


    # Display the frame and recognized text
    cv2.imshow('Frame', frame)
    if (text!=""):
        print("Recognized Text:", text)
        speak(text)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
