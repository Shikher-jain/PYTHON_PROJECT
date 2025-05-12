# import tkinter as tk

# root = tk.Tk()

# text = tk.Text(root)
# text.insert(1.0, "Hello, world!")
# text.delete("1.3", "end")
# text
# text.see("end-1c")

# text.pack()

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()

# text = tk.Text(root)
# text.insert("1.0", "Hello, world!")
# text.insert("end", "This is a test.\n")
# text.insert("end", "This is another test.\n")
# text.insert("end", "This is the last test.\n")

# # Delete all text in the widget
# btn=tk.Button(root,text="del",command=lambda:text.delete(1.0, "end"))
# text.pack()
# text.delete("1.0", "end")
# btn.pack()

# root.mainloop()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg = '#d3f3f5')
root.title('Contact Book')
root.resizable(0,0)
contactlist = []
    # ['Siddharth Nigam','369854712'],
    # ['Gaurav Patil', '521155222'],
    # ['Abhishek Nikam', '78945614'],
    # ['Sakshi Gaikwad', '58745246'],
    # ['Mohit Paul', '5846975'],
    # ['Karan Patel', '5647892'],
    # ['Sam Sharma', '89685320'],
    # ['John Maheshwari', '98564785'],
    # ['Ganesh Pawar','85967412']
    # ]
 
Name = StringVar()
Number = StringVar()
Email = StringVar()
address_e=StringVar()

frame = Frame(root,bg="#d3f3f5")
frame.pack(side = RIGHT)
 
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman' ,10), bg="#f0fffc", width=40, height=40, bd=3, relief= "groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1,pady=20)

def Selected():
    if len(select.curselection())==0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

def AddContact():
    if Name.get()!="" and Number.get()!="" and Email.get()!="" and address_e.get(1.0, END)!="":
        contactlist.append([Name.get() ,Number.get(),Email.get(),address_e.get(1.0, END)])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
    else:
        messagebox.showerror("Error","Please fill the information")
 
def UpdateDetail():
    if Name.get() and Number.get() and Email.get() and address_e.get(1.0, END):
        contactlist[Selected()] = [Name.get(), Number.get(),Email.get(),address_e.get(1.0, END)]
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()
 
    elif not(Name.get()) and not(Number.get()) and not(Email.get()) and not(address_e.get(1.0,END)) and not(len(select.curselection())==0):
        messagebox.showerror("Error", "Please fill the information")
 
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)

def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

def VIEW():
    NAME, PHONE, EMAIL, ADDRESS = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Email.set(EMAIL)
    address_e.insert(1.0,ADDRESS)

def EXIT():
    root.destroy() 
 
def EntryReset():
    Name.set('')
    Number.set('')
    Email.set('')
    address_e.delete(1.0,END)
    
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    # for name,phone in contactlist :
    for name in contactlist :
        select.insert (END, name)
Select_set()

Label(root, text = 'Name', font=("Times new roman",22,"bold"),bg = '#d3f3f5').place(x= 30, y=20)
Entry(root, textvariable = Name, width=34).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",20,"bold"),bg = '#d3f3f5').place(x= 30, y=70)
Entry(root, textvariable = Number, width=34).place(x= 200, y=80)
Label(root, text = 'Email.', font=("Times new roman",20,"bold"),bg = '#d3f3f5').place(x= 30, y=120)
Entry(root, textvariable = Email, width=34).place(x= 200, y=130)
Label(root, text = 'Address', font=("Times new roman",20,"bold"),bg = '#d3f3f5').place(x= 30, y=170)
address_e=Text(root, height=10,width=25)
address_e.place(x= 200, y=180)

Button(root,text=" ADD", font='Helvetica 18 bold',bg='#e8c1c7', command = AddContact,width=10).place(x= 50, y=360)
Button(root,text="EDIT", font='Helvetica 18 bold',bg='#e8c1c7',command = UpdateDetail, width=10).place(x= 250, y=360)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = Delete_Entry, width=10).place(x=50 , y=420)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#e8c1c7', command = VIEW,width=10).place(x= 250, y=420)
Button(root,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = EntryReset,width=10).place(x= 50, y=480)
Button(root,text="EXIT", font='Helvetica 18 bold',bg='tomato', command = EXIT,width=10).place(x= 250, y=480)
 
root.mainloop()