import cv2
import pytesseract
import os

# Optional: If using Windows and Tesseract is not in PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create folder to save scanned plates
os.makedirs("Resources/Scanned", exist_ok=True)

# Frame and detection settings
frameWidth = 640
frameHeight = 480
minArea = 200
color = (255, 0, 255)

# Load Haar Cascade
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

# Load video
cap = cv2.VideoCapture("Resources/video12.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    if not success:
        print("Video ended or cannot be loaded.")
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)

    imgRoi = None  # Reset ROI

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

            # OCR preprocessing
            plate_gray = cv2.cvtColor(imgRoi, cv2.COLOR_BGR2GRAY)
            _, plate_thresh = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)

            # Extract text with Tesseract
            text = pytesseract.image_to_string(plate_thresh, config='--psm 8')
            text = text.strip()

            # Print and display text
            print(f"[INFO] Detected Plate Text: {text}")
            cv2.putText(img, text, (x, y + h + 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Result", img)

    # Save the plate on pressing 's'
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s') and imgRoi is not None:
        filename = f"Resources/Scanned/NoPlate_{count}.jpg"
        cv2.imwrite(filename, imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265),
                    cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
