from tkinter import *
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.resizable(width=False,height=False)
        self.root.config(bg="#05192A")
        self.tasks = []
 
        f=Frame(self.root,bg="#7CA5B3",bd=5,relief="groove")
        self.task_list = Listbox(f ,bg="#B7C8CE",width=40, height=10,font=( 'Comic Sans MS' ,'8', 'bold'))
        self.task_list.pack(padx=5, pady=5)
        f.pack(padx=10,pady=10)
        self.entry = Entry(self.root,bg="#B7C8CE",width=37,bd=4,relief="sunken",font=( 'Comic Sans MS' ,'10', 'bold'))
        self.entry.pack(padx=10, pady=(0,10))

        btnsF=Frame(self.root,bg="#7CA5B3",bd=6,relief="groove")
        self.add_button =    Button(btnsF, text="Add\nTask",bd=5,relief="raised",width=7, command=self.add_task)
        self.delete_button = Button(btnsF, text="Delete\nTask",bd=5,relief="raised",width=7, command=self.delete_task)
        self.mark_button =   Button(btnsF, text="Mark as\nDone",bd=5,relief="raised",width=7, command=self.mark_done)
        self.for_exit_btn=   Button(btnsF, text="EXIT",pady=8, command = self.for_exit,bd=5,relief="raised",width=7)

        self.add_button.grid   (row=0,column=0,padx=(10,5), pady=10)
        self.delete_button.grid(row=0,column=1,padx=5, pady=10)
        self.mark_button.grid  (row=0,column=2,padx=5, pady=10)
        self.for_exit_btn.grid (row=0,column=3,padx=(5,10), pady=10)
        btnsF.pack(pady=(0,10))

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        
        try:
            task_index = self.task_list.curselection()[0]
            self.tasks.pop(task_index)
            self.task_list.delete(task_index)
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete")

    def mark_done(self): 
        try:
            task_index = self.task_list.curselection()[0]
            if self.tasks[task_index][:6]!="[Done]":
                self.tasks[task_index] = f"[Done] {self.tasks[task_index]}"
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, self.tasks[task_index])
            else:
                messagebox.showerror("ERROR","  Already Mark As Done  ")
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as done")
    def for_exit(self):
        result=messagebox.askyesno("CONFIRMAATION","Do you want to Exit:")
        if result==True:
            self.root.destroy()
        else:
            pass
if __name__ == "__main__":
    root = Tk()
    todo_list = ToDoList(root)
    root.mainloop()