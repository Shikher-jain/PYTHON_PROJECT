from tkinter import *
import tkinter as messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.resizable(width=False,height=False)
        self.tasks = []

        self.task_list = Listbox(self.root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        self.entry = Entry(self.root, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.mark_button = Button(self.root, text="Mark as Done", command=self.mark_done)
        self.mark_button.pack(padx=10, pady=10)

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
            task = self.tasks[task_index]
            self.tasks[task_index] = f"[Done] {task}"
            self.task_list.delete(task_index)
            self.task_list.insert(task_index, self.tasks[task_index])
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as done")

if __name__ == "__main__":
    root = Tk()
    todo_list = ToDoList(root)
    root.mainloop()