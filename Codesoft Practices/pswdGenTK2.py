from tkinter import *
import random
import string

def pswdGen(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password

def pswdCpy():
    root.clipboard_clear() #to clear previous copied data in clipboard
    root.clipboard_append(pswd_e.get())
    root.update() #here the pswd is copied to past somewhere

root =Tk()
root.title("Password Generator")

len_lbl =Label(root, text="Password Length:")
len_lbl.pack()

len_e =Entry(root, width=5)
len_e.pack()

gen_btn =Button(root, text="Generate Password", command=lambda: pswd_e.delete(0,END) or pswd_e.insert(0, pswdGen(int(len_e.get()))))
gen_btn.pack()

pswd_e = Entry(root, width=20)
pswd_e.pack()

cpybtn =Button(root, text="Copy to Clipboard",command=pswdCpy)
cpybtn.pack()

root.mainloop()

