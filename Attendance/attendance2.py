import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os

# CSV file path
filename = r"F:\SHIKHER-VS\Advance-Python-SJ\Projects\Attendance\attendance2.csv"

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

    messagebox.showinfo("✅ Success", f"Attendance marked for {name} as {status}")
    entry_name.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("📝 Attendance System")
root.geometry("400x320")
root.resizable(False, False)
root.config(bg="#e6f7ff")

# Header Frame
header_frame = tk.Frame(root, bg="#0099cc")
header_frame.pack(fill="x")

tk.Label(header_frame, text="📝 Attendance System", font=("Arial", 18, "bold"), bg="#0099cc", fg="white").pack(pady=10)

# Date & Time Display
now = datetime.now()
current_date = now.strftime("%d %B %Y")
current_time = now.strftime("%I:%M %p")

tk.Label(root, text=f"📅 {current_date}", font=("Arial", 10), bg="#e6f7ff", fg="black").pack(pady=(5, 0))
tk.Label(root, text=f"🕒 {current_time}", font=("Arial", 10), bg="#e6f7ff", fg="black").pack(pady=(0, 10))

# Input Section
form_frame = tk.Frame(root, bg="#e6f7ff")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Enter your name:", font=("Arial", 12), bg="#e6f7ff").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(form_frame, font=("Arial", 12), width=28)
entry_name.grid(row=1, column=0, padx=10, pady=5)

var_status = tk.StringVar(value="Present")

tk.Label(form_frame, text="Status:", font=("Arial", 12), bg="#e6f7ff").grid(row=2, column=0, sticky="w", pady=(10, 0))
tk.Radiobutton(form_frame, text="✅ Present", variable=var_status, value="Present", font=("Arial", 11), bg="#e6f7ff").grid(row=3, column=0, sticky="w", padx=20)
tk.Radiobutton(form_frame, text="❌ Absent", variable=var_status, value="Absent", font=("Arial", 11), bg="#e6f7ff").grid(row=4, column=0, sticky="w", padx=20)

# Submit Button
tk.Button(root, text="Mark Attendance", font=("Arial", 15, "bold"), command=mark_attendance,bg="#28a745", fg="white",height=15 ,width=20, relief="flat", cursor="hand2").pack(pady=5)

# Footer
tk.Label(root, text="Created by Shikher Jain", font=("Arial", 9), bg="#e6f7ff", fg="#888").pack(side="bottom", pady=5)

root.mainloop()
