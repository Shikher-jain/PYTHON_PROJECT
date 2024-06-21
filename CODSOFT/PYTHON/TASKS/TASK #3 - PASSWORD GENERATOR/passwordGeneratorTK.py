import array
import random
from tkinter import *
from tkinter import messagebox

def display(rawPswd):
    password=""
    for i in rawPswd:
        password+=i
    e.delete(0,END)
    e.insert(0,password[:])
    
def pswdCpy():
    root.clipboard_clear() #to clear previous copied data in clipboard
    root.clipboard_append(e.get())
    root.update() #here the pswd is copied to past somewhere
    l.delete(0,END)
    e.delete(0,END)

def con(l):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
    upper_chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
    spe_symbols=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[','{',']','}','\\','|',';',':','"',"'",'/','?','.','>',',','>']

    combination = digits + upper_chr + lower_chr + spe_symbols 

    rand_digit = random.choice(digits) 
    rand_upper = random.choice(upper_chr) 
    rand_lower = random.choice(lower_chr) 
    rand_symbol = random.choice(spe_symbols) 

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

    try:
        l=int(l)
        if(l>4):
            for temp in range(l-4):
                temp_pass+=random.choice(combination)
                rawPswd=array.array("u",temp_pass)
                random.shuffle(rawPswd)
            display(rawPswd)
        elif(l==4):
            rawPswd=array.array("u",temp_pass)
            random.shuffle(rawPswd) 
            display(rawPswd)
        else:
            e.delete(0,END)
            messagebox.showerror("Error","Enter Valid Length (i.e. : >= 4)")
    except :
        l=str(l)
        messagebox.showerror("Value Error","Enter Only Integer Value..")
def EXIT():
    result=messagebox.askyesno("CONFIRMAATION","Do you want to Exit:")
    if result==True:
        root.destroy()
    else:
        pass


root=Tk()  
root.title("Password Generator")
root.config(bg="#010B13",padx=10,pady=10)
root.resizable(width=False,height=False)

txt=Label(text="PASSWORD GENERATOR",bg="#010B13",fg="red",font="Ubuntu 15 bold")
txt_l=Label(text="Enter Password Lenght",bg="#010B13",fg="white",font="typewriter 10 bold")
l=Entry(root,bd=5,bg="#B7C8CE",font="Ubuntu 15 bold")

l_btn=Button(root,text="Generate Password",bg="#010B13",fg="white",relief="flat",command=lambda:con(l.get()))
e=Entry(root,bd=5,relief="ridge",bg="#B7C8CE",font="Ubuntu 15 bold")
cpyBn=Button(root,text="Copy To Clipboard",bg="#010B13",fg="white",relief="flat",command=pswdCpy)
exitBn=Button(root,text="Exit",bg="#010B13",fg="white",relief="flat",command=EXIT)

txt.grid     (row=0, column=0,pady=(0,10))
txt_l.grid   (row=1, column=0)
l.grid       (row=2, column=0)
l_btn.grid   (row=3, column=0) 
e.grid       (row=4, column=0)
cpyBn.grid   (row=5, column=0)
exitBn.grid  (row=6, column=0)

root.mainloop()