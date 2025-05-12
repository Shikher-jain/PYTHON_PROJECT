from tkinter import *
root=Tk()
root.config(bg="#061d2f")
datas = [] 

def add(): 
	global datas 
	datas.append(Name.get()) 
	update() 

def view(): 
	Name.set(datas[int(select.curselection()[0])][0]) 
	
def delete():
	del datas[int(select.curselection()[0])] 
	update() 

def reset(): 
	Name.set('') 
	
def update(): 
	select.delete(0,END) 
	for n in datas: 
		select.insert(END, n) 

Name = StringVar()  

FONT='arial 12 bold'

Label(root, text = 'Name',bd=2 ,relief="raised",bg="#061d2f",fg="white",width=8,font=FONT).pack(pady=(10,5))
Entry(root, textvariable = Name,width=38).pack(pady=(5,5))

F=Frame(root)
Button(F,text="Add",   bg="#353535",fg="#B7C8CE",font="arial 12 bold",width=5,command=add,).grid(row=0,column=0)
Button(F,text="View",  bg="#353535",fg="#B7C8CE",font="arial 12 bold",width=5,command=view,).grid(row=0,column=1)
Button(F,text="Delete",bg="#353535",fg="#B7C8CE",font="arial 12 bold",width=5,command=delete,).grid(row=0,column=2)
Button(F,text="Reset", bg="#353535",fg="#B7C8CE",font="arial 12 bold",width=5,command=reset,).grid(row=0,column=3)
F.pack(pady=(5,10))

scroll_bar = Scrollbar(root, orient=VERTICAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=X) 
select.pack() 

root.mainloop()

print(datas)