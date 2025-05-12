import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os 

# CSV file path
filename = r"F:\SHIKHER-VS\Advance-Python-SJ\Projects\Attendance\attendance.csv"

# Create file with headers if it doesn't exist
if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])

# Mark Attendance Function
def mark_attendance():
    name = entry_name.get().strip()
    status = var_status.get()

    if name == "":
        messagebox.showwarning("Input Error", "Please enter your name!")
        return

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time, status])

    messagebox.showinfo("Success", f"Attendance marked for {name} as {status}")
    entry_name.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Attendance System")
root.geometry("350x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Attendance System", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Enter your name:", bg="#f0f0f0").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

var_status = tk.StringVar(value="Present")
tk.Radiobutton(root, text="Present", variable=var_status, value="Present", bg="#f0f0f0").pack()
tk.Radiobutton(root, text="Absent", variable=var_status, value="Absent", bg="#f0f0f0").pack()

tk.Button(root, text="Mark Attendance", command=mark_attendance, bg="green", fg="white").pack(pady=10)

root.mainloop()
