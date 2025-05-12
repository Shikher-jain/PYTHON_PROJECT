import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):

        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("450x305")
        self.root.resizable(width=False,height=False)

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x")

        self.frame2 = tk.Frame(self.root) 
        self.frame2.pack(fill="x")

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x")

        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(fill="x")

        tk.Label(self.frame1, text="Name:",width=8,justify="right",pady=5).pack(side="left")
        self.name_entry = tk.Entry(self.frame1, width=30,bd=1,relief="solid")
        self.name_entry.pack(side="left",padx=(0,10))

        tk.Label(self.frame2, text="Phone:",width=8,justify="right",pady=5).pack(side="left")
        self.phone_entry = tk.Entry(self.frame2, width=30,bd=1,relief="solid")
        self.phone_entry.pack(side="left",padx=(0,10))

        tk.Label(self.frame3, text="Email:",width=8,justify="right",pady=5).pack(side="left")
        self.email_entry = tk.Entry(self.frame3, width=30,bd=1,relief="solid")
        self.email_entry.pack(side="left",pady=10,padx=(0,10))

        tk.Label(self.frame4, text="Address:",width=8,justify="right",pady=5).pack(side="left")
        self.address_entry = tk.Text(self.frame4, width=22,height=10,bd=1,relief="solid")
        self.address_entry.pack(side="left",pady=(0,10),padx=(0,10))

        self.lst=tk.Listbox(self.root,width=30,height=15,bd=5,relief="sunken")
        self.lst.place(x=250,y=5)
        
        root2=tk.Frame(self.root)
        root2.place(y=270,x=20)

        self.btn_frame=tk.Frame(root2)

        tk.Button(self.btn_frame, text="Add Contact", width=11, command=self.add_contact).grid(row=0,column=0)
        tk.Button(self.btn_frame, text="View Contacts", width=11, command=self.view_contacts).grid(row=0,column=1)
        tk.Button(self.btn_frame, text="Update", width=11, command=self.update).grid(row=0,column=2)
        tk.Button(self.btn_frame, text="Exit", width=11, command=self.root.destroy).grid(row=0,column=3)

        self.contact_list = ""
        self.btn_frame.grid(row=0,column=0)
        self.contacts = []


    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address=self.address_entry.get(1.0,tk.END)

        if name and phone and email and address:
            global contacts
            self.contacts.append({"name": name, "phone": phone, "email": email, "address":address})
            self.name_entry.delete(0,"end")
            self.phone_entry.delete(0,"end")
            self.email_entry.delete(0,"end")
            self.address_entry.delete(0.0,"end")
            messagebox.showinfo("Success","Contact added successfully!") 
        else:
            messagebox.showerror("Error","Please fill in all fields!")

    def view_contacts(self):
        # global contact_list 
        for contact in self.contacts:
            self.contact_list += f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress:{contact['address']}\n"
            
        messagebox.showinfo("Contacts", self.contact_list)
    def update(self):
        try:
            if (len(self.contacts)):
                for i in range(len(self.contacts)):
                    self.lst.insert(tk.END,f'{self.contacts[i]['name']}')
            else:
                messagebox.showerror("Error","No More Contacts To Update")
        except ValueError:
                messagebox.showerror("Error","No More Contacts To Update")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()