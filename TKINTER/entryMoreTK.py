import tkinter as tk
import math
root = tk.Tk()

# root.geometry("300x350")

# Label1 = tk.Label(root, text="insertborderwidth ").grid(row=0, column=0)
# Entry1 = tk.Entry(root , insertwidth=2).grid(row=0, column=1,padx=15 , pady=20)


print("log\u2081\u2080  log\u2082")
print("x\u00B2 x\u00B3")
print("x\u00B1 x\xb9")
print("x\u207b\xb9")
print("")
print("")


IP_txt = tk.StringVar()
n=[1,2,3,4,5,6,7,8,9,0]
def inv():
    global calc_op
    result = str(math.pow(int(calc_op),-1))
    calc_op = result
    IP_txt.set(calc_op)
txt_entry = tk.Entry(root, font=('sans-serif', 20, 'bold'), bd=5, bg='#BBB').grid(row=0,column=0,columnspan=6)

for i in range(1,6):
    for j in range(6):
        tk.Button(root,text=n[j],height=2,width=5,command=inv).grid(row=i, column=j)
calc_op = ""
root.mainloop()