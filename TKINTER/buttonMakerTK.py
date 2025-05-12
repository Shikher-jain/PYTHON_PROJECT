from tkinter import *
import math

root =  Tk()
root.title('Scientific Calculator')
root.configure(bg='#061D2F')
root.resizable(width=False, height=False)

numberpad = ['CE','CE','\u221A','+','\u03C0','e','Deg','x\u00B2','7','8','9','-','Exp','x!','Rad','x\u00B3','4','5','6','x','sin','con','tan',"10\u207F",'1','2','3','/','sinh','cosh','tanh','1/x','0','0','.','=','ln','log2','log10','Abs']
i = 0
# print((len(numberpad)))#40
button = []
for j in range(2,7):    #row
    for k in range(8):  #column
        if i==0 or i==32:
            button.append( Button(root, text=numberpad[i], font=('Arial', 10, 'bold'),fg="red", width=20, height=3,highlightbackground='#156247', highlightthickness=2))
            button[i].grid(row=j, column=k , padx=10, pady=10,columnspan=2)
            # button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
            i+=1
            k-=2
        else:
            button.append( Button(root, text=numberpad[i], font=('Arial', 10, 'bold'),fg="red", width=8, height=3,highlightbackground='#156247', highlightthickness=2))
            button[i].grid(row=j, column=k, sticky='nsew', padx=10, pady=10)
            # button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
            i += 1


root.mainloop()