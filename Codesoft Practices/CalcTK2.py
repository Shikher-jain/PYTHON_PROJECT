from tkinter import *
import math
from turtle import width

def btn_click(char):
    global calc_op
    calc_op += str(char)
    IP_txt.set(calc_op)
    
def btn_clr():
    global calc_op
    calc_op = ""
    IP_txt.set("")

def btn_dlt():
    global calc_op
    text = calc_op[:-1]
    calc_op = text
    IP_txt.set(text)


def sign_chng():
    global calc_op
    if calc_op[0]=='-':
        temp = calc_op[1:]
    else:
        temp = '-'+calc_op
    calc_op = temp
    IP_txt.set(temp)    

def button_equal():
    global calc_op
    try:
        temp_op = str(eval(calc_op))
        IP_txt.set(temp_op)
        calc_op = temp_op
    except:
        calc_op="ERROR"
        IP_txt.set("ERROR")

root = Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Scientific Calculator")

calc_op = ""
IP_txt = StringVar()

txt_entry = Entry(root, font=('sans-serif', 20, 'bold'), textvariable=IP_txt,bd=5, insertwidth = 5, bg="#B7C8CE",width=30 ,justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold'),"width":2}

button_7 = Button(root, button_params_main, text='7',command=lambda:btn_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(root, button_params_main, text='8',command=lambda:btn_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(root, button_params_main, text='9',command=lambda:btn_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(root, button_params_main,text='DEL', command=btn_dlt, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(root, button_params_main,text='AC', command=btn_clr, bg='#db701f').grid(row=6, column=4, sticky="nsew")

button_4 = Button(root,button_params_main, text='4',command=lambda:btn_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(root,button_params_main, text='5',command=lambda:btn_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(root,button_params_main, text='6',command=lambda:btn_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(root, button_params_main, text='*',command=lambda:btn_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(root, button_params_main, text='/',command=lambda:btn_click('/')).grid(row=7, column=4, sticky="nsew")

button_1 = Button(root, button_params_main, text='1',command=lambda:btn_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(root, button_params_main, text='2',command=lambda:btn_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(root, button_params_main, text='3',command=lambda:btn_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(root, button_params_main, text='+',command=lambda:btn_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(root, button_params_main, text='-',command=lambda:btn_click('-')).grid(row=8, column=4, sticky="nsew")

point = Button(root, button_params_main, text='.',command=lambda:btn_click('.')).grid(row=9, column=1, sticky="nsew")
button_0 = Button(root, button_params_main, text='0',command=lambda:btn_click('0')).grid(row=9, column=0, sticky="nsew")
signs = Button(root, button_params_main, text='\u00B1',command=sign_chng).grid(row=9, column=2, sticky="nsew")
equal = Button(root, button_params_main, text='=',command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")

root.mainloop()