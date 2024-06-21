from tkinter import *
from tkinter import messagebox

class Calculator:
    def __init__(self, root):  
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(width=False,height=False)
        self.root.config(bg="#061d2f")
        
        f=Frame(self.root ,bg="#061d2f")
        self.entry = Entry(self.root,width=29,bd=4,relief="sunken",bg="#B7C8CE")
 
        self.entry.grid(padx=(0,40),pady=8,row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            '%'# 'CLEAR ', '<<'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            Button(f, text=button, width=5,bd=4,relief="raised", command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val,padx=5,pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        Button(f, text="Clear", width=13,bd=4,relief="raised", command=self.clear).grid(row=row_val, column=1, columnspan=2)

        Button(f, text="<<", width=5,bd=4,relief="raised", command=self.back).grid(row=row_val, column=3)
        f.grid()
        Button(root,text="Exit",command=self.exit_root,bd=4,relief="raised").place(x=196,y=8)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(END, result)
            except Exception as e:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
        else:
            self.entry.insert(END, button)

    def clear(self):
        self.entry.delete(0, END)

    def back(self):
        rec=self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0,rec[:-1])

    def exit_root(self):
        result=messagebox.askyesno("CONFIRMAATION","Do you want to Exit:")
        if result==True:
            self.root.destroy()
        else:
            pass

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()