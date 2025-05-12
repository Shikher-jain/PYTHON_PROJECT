import tkinter as tk
from tkinter import messagebox

class ContactBook:
    contact_list = ""
    i=0
    with open("Shikher-jain/CODSOFT/PYTHON/CONTACT.txt",'a') as file:    
        file.write("(name,phone,email,address)"+"\n")        
    def __init__(self, root):
        self.root = root
        self.root.config(bg="blue")
        self.root.title("Contact Book")
        self.lst=tk.Listbox(self.root,width=40)
        self.lst.pack(side="left")
        
        root2=tk.Frame(self.root)
        root2.place(y=240,x=20)

        self.btn_frame=tk.Frame(root2)

        tk.Button(self.btn_frame, text="Add Contact", width=11).grid(row=0,column=0)
        tk.Button(self.btn_frame, text="View Contacts", width=11).grid(row=0,column=1)
        tk.Button(self.btn_frame, text="Update", width=11).grid(row=0,column=2)
        tk.Button(self.btn_frame, text="Exit", width=11).grid(row=0,column=3)

        self.btn_frame.grid(row=0,column=0)
        self.contacts = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()



# -------------------------------------------------------------


        # with open("Shikher-jain/CODSOFT/PYTHON/CONTACT.txt",'a') as file:    
        #     file.write("(name,phone,email,address)"+"\n")        

                
        # with open("Shikher-jain/CODSOFT/PYTHON/CONTACT.txt",'a') as file:
        #     for contact in self.contacts:
        #         file.write(f"({contact['name']},{contact['phone']},{contact['email']},{contact['address']})"+"\n")

