import tkinter as tk

root = tk.Tk()

# frame = tk.Frame(root, width=200, height=100)
# frame.pack()

label = tk.Label(root, text="Hello, World!")
label.grid(sticky='n'+'s'+'e'+'w')

root.mainloop()