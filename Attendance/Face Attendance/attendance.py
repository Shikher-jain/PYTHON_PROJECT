import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import cv2
import face_recognition
import os
import numpy as np
import csv

# Path settings
CSV_PATH = r"F:\SHIKHER-VS\Advance-Python-SJ\Projects\Attendance\Face Attendance\attendance01.csv"
FACES_DIR = r"F:\SHIKHER-VS\Advance-Python-SJ\Projects\Attendance\Face Attendance\faces"

# Create CSV if not exists
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])

# Load known faces
known_face_encodings = []
known_face_names = []

for filename in os.listdir(FACES_DIR):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file(os.path.join(FACES_DIR, filename))
        encoding = face_recognition.face_encodings(image)
        if encoding:
            known_face_encodings.append(encoding[0])
            known_face_names.append(os.path.splitext(filename)[0])

# Face Recognition Function
def recognize_and_mark():
    cap = cv2.VideoCapture(0)
    recognized = set()

    while True:
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, faces)

        for face_encoding in encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_dist = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match = np.argmin(face_dist)

            if matches[best_match]:
                name = known_face_names[best_match]

                if name not in recognized:
                    now = datetime.now()
                    date = now.strftime("%Y-%m-%d")
                    time = now.strftime("%H:%M:%S")

                    with open(CSV_PATH, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([name, date, time, "Present"])

                    recognized.add(name)
                    cv2.putText(frame, f"{name} Marked Present", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, f"{name} Already Marked", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            else:
                cv2.putText(frame, "Unknown Face", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        cv2.imshow('Face Recognition - Press Q to Exit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Done", "Face attendance process completed!")

# GUI Part
root = tk.Tk()
root.title("Attendance System with Face Recognition")
root.geometry("400x300")
root.config(bg="#e6f7ff")

tk.Label(root, text="📝 Attendance System", font=("Arial", 18, "bold"), bg="#0099cc", fg="white").pack(fill="x", pady=10)

tk.Button(root, text="📸 Start Face Recognition", command=recognize_and_mark,
          font=("Arial", 13, "bold"), bg="#28a745", fg="white", width=25).pack(pady=50)

tk.Label(root, text="Make sure your image is in 'faces/' folder with your name!", bg="#e6f7ff", fg="#666", font=("Arial", 9)).pack(pady=10)

root.mainloop()
