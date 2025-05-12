from tkinter import *
from tkinter import messagebox
import random

n = random.randint(0, 100)
guesses = 1
a = -1
def Guess():
    global guesses
    global a
    try:
        while(a != n):
            a=entry.get()
            if(a >n):
                guesses +=1
                messagebox.showinfo("INSTRUCTION","Lower number please")
            elif(a<n):
                guesses +=1
                messagebox.showinfo("INSTRUCTION","Higher number please")
            entry.set("")
        messagebox.showinfo("Congratulation",f"You have guessed the number {n} correctly in {guesses} attempts")
        root.destroy()

    except TypeError:
        messagebox.showerror("ERROR","Enter Integer Value Only\nor\nFirst Enter Integer Value")
        # messagebox.showerror("ERROR","Enter Integer Value Only\nor\nFirst Enter Integer Value")

root=Tk()
entry=IntVar()
Label(root,text="Guess the number:").pack()
Entry(root,textvariable=entry).pack()
Button(root,text="Enter",bd=3,relief="raised",command=lambda:Guess()).pack()
root.mainloop()