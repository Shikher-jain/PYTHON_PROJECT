from tkinter import*

root=Tk()
root.title("CALCULATOR")
root.geometry("480x460") 

F1=LabelFrame(root,bd=15,bg="#010B13",relief=SUNKEN,fg="white")
F1.place(width=480,height=460)

lbl=Label(F1,padx=0,pady=0)
lbl.grid(pady=40)

entry1=Entry(F1,relief=GROOVE,font=("arial 24"))
entry1.place(x=35,y=15,width=380,height=70) 


def button_click(num):
    rec=entry1.get() #recent sign or no.
    entry1.delete(0, END)
    entry1.insert(0, str(rec) + str(num))
    
def button_equal():
    try:
        rec=entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,eval(rec))
    except:
        entry1.delete(0,END)
        entry1.insert(0,"ERROR")

def button_backspace():
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, current[:-1])  


def button_clear():
    entry1.delete(0,END)

button_4 = Button(F1,text="4", padx=40, pady=20, command=lambda: button_click(4) ,bg="gray",fg="white")
button_2 = Button(F1,text="2", padx=40, pady=20, command=lambda: button_click(2) ,bg="gray",fg="white")
button_1 = Button(F1,text="1", padx=40, pady=20, command=lambda: button_click(1) ,bg="gray",fg="white")
button_5 = Button(F1,text="5", padx=40, pady=20, command=lambda: button_click(5) ,bg="gray",fg="white")
button_6 = Button(F1,text="6", padx=40, pady=20, command=lambda: button_click(6) ,bg="gray",fg="white")
button_3 = Button(F1,text="3", padx=40, pady=20, command=lambda: button_click(3) ,bg="gray",fg="white")
button_7 = Button(F1,text="7", padx=40, pady=20, command=lambda: button_click(7) ,bg="gray",fg="white")
button_8 = Button(F1,text="8", padx=40, pady=20, command=lambda: button_click(8) ,bg="gray",fg="white")
button_9 = Button(F1,text="9", padx=40, pady=20, command=lambda: button_click(9) ,bg="gray",fg="white")
button_0 = Button(F1,text="0", padx=40, pady=20, command=lambda: button_click(0) ,bg="gray",fg="white")

button_subtract = Button(F1, text="-", padx=41, pady=20, command=lambda: button_click("-") ,bg="gray",fg="white")
button_multiply = Button(F1, text="*", padx=41, pady=20, command=lambda: button_click("*") ,bg="gray",fg="white")
button_divide =   Button(F1, text="/", padx=41, pady=20, command=lambda: button_click("/") ,bg="gray",fg="white")
button_add =      Button(F1, text="+ ", padx=38, pady=20, command=lambda: button_click("+") ,bg="gray",fg="white")
button_dot =      Button(F1, text=" .", padx=40, pady=20, command=lambda: button_click(".") ,bg="gray",fg="white")

button_backspace =Button(F1, text="<<",padx=35, pady=20, command=button_backspace ,bg="gray",fg="white")
button_equal =    Button(F1, text="=",     padx=87, pady=20, command=button_equal ,bg="gray",fg="white")
button_clear =    Button(F1, text="Clear", padx=77, pady=20, command=button_clear ,bg="gray",fg="white")



button_backspace.grid(row=1, column=0,padx=(35,0))
button_clear.grid(row=1, column=1,columnspan=2)
button_divide.grid(row=1, column=3)

button_7.grid(row=4, column=0,padx=(35,0))
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_4.grid(row=5, column=0,padx=(35,0))
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_multiply.grid(row=5, column=3)

button_1.grid(row=6, column=0,padx=(35,0))
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_add.grid(row=6,column=3)

button_dot.grid(row=7, column=0,padx=(35,0))
button_0.grid(row=7, column=1)
button_equal.grid(row=7, column=2,columnspan=2)

buttons_no=[button_dot,button_0,button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]

buttons_op=[button_subtract,button_add,button_multiply,button_divide]

def hover(button,entryBG,entryFG,leaveBG,leaveFG):
    button.bind("<Enter>",func=lambda e: button.config(bg=entryBG,fg=entryFG))
    button.bind("<Leave>",func=lambda e: button.config(bg=leaveBG,fg=leaveFG))
for i in buttons_no:
    hover(i,"#606573","#000000","gray","white")
for i in buttons_op:
    hover(i,"#F77B00","#261C62","gray","white")
hover(button_equal,"#0BDA72","black","gray","white")
hover(button_clear,"#BD1616","#B89D05","gray","white")
hover(button_backspace,"#0A4ECC","#B89D05","gray","white")
root.mainloop()