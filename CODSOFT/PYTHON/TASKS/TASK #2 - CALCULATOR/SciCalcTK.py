from tkinter import *
from tkinter import messagebox
import math

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

def fact_func():
    global calc_op
    result = str(math.factorial(int(calc_op)))
    calc_op = result
    IP_txt.set(result)
    
def trig_sin():
    global calc_op
    result = str(math.sin(math.radians(int(calc_op))))
    calc_op = result
    IP_txt.set(result)

def trig_cos():
    global calc_op
    result = str(math.cos(math.radians(int(calc_op))))
    calc_op = result
    IP_txt.set(result)

def trig_tan():
    global calc_op
    result = str(math.tan(math.radians(int(calc_op))))
    calc_op = result
    IP_txt.set(result)

def sq_root():
    global calc_op
    if (float(calc_op)>=0):
        temp = str(eval(calc_op+'**(1/2)'))
        calc_op = temp
    else:
        temp = "ERROR"
    IP_txt.set(temp)

def cube_root():
    global calc_op
    if float(calc_op)>=0:
        temp = str(eval(calc_op+'**(1/3)'))
        calc_op = temp
    else:
        temp = "ERROR"
    IP_txt.set(temp)

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

def exit_root():
    result=messagebox.askyesno("CONFIRMAATION","Do you want to Exit:")
    if result==True:
        root.destroy()
    else:
        pass

sin, cos, tan = math.sin, math.cos, math.tan
log10,log2 ,ln = math.log10,math.log2, math.log
e = math.exp
p = math.pi
E = '10*'

root = Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Scientific Calculator")

calc_op = ""
IP_txt = StringVar()

txt_entry = Entry(root, font=('sans-serif', 20, 'bold'), textvariable=IP_txt,bd=5, insertwidth = 5, bg="#B7C8CE",width=30 ,justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

#--1st row--

abs_value = Button(root, button_params, text='abs',command=lambda:btn_click('abs(')).grid(row=1, column=0, sticky="nsew")
modulo = Button(root, button_params, text='mod',command=lambda:btn_click('%')).grid(row=1, column=1, sticky="nsew")
int_div = Button(root, button_params, text='div',command=lambda:btn_click('//')).grid(row=1, column=2, sticky="nsew")
factorial_button = Button(root, button_params, text='x!',command=fact_func).grid(row=1, column=3, sticky="nsew")
Button(root,button_params,text="EXIT",command=exit_root,relief="raised",bg="#B63232").grid(row=1, column=4, sticky="nsew")

#--2nd row--

sine = Button(root, button_params, text='sin',command=trig_sin).grid(row=2, column=0, sticky="nsew")
cosine = Button(root, button_params, text='cos',command=trig_cos).grid(row=2, column=1, sticky="nsew")
tangent = Button(root, button_params, text='tan',command=trig_tan).grid(row=2, column=2, sticky="nsew")
log_basee = Button(root, button_params, text='ln',command=lambda:btn_click('ln(')).grid(row=2, column=3, sticky="nsew")
pi_num = Button(root, button_params, text='π',command=lambda:btn_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

#--3rd row--

second_power = Button(root, button_params, text='x\u00B2',command=lambda:btn_click('**2')).grid(row=3, column=0, sticky="nsew")
third_power = Button(root, button_params, text='x\u00B3',command=lambda:btn_click('**3')).grid(row=3, column=1, sticky="nsew")
nth_power = Button(root, button_params, text='x^n',command=lambda:btn_click('**')).grid(row=3, column=2, sticky="nsew")
inv_power = Button(root, button_params, text='x\u207b\xb9',command=lambda:btn_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
tens_powers = Button(root, button_params, text='10^x', font=('sans-serif', 15, 'bold'),command=lambda:btn_click('10**')).grid(row=3, column=4, sticky="nsew")

#--4th row--

sq_root = Button(root, button_params, text='\u00B2\u221A',command=sq_root).grid(row=4, column=0, sticky="nsew")
cube_root = Button(root, button_params, text='\u00B3\u221A',command=cube_root).grid(row=4, column=1, sticky="nsew")
nth_root = Button(root, button_params, text='\u221A',command=lambda:btn_click('**(1/')).grid(row=4, column=2, sticky="nsew")
log_base10 = Button(root, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),command=lambda:btn_click('log10(')).grid(row=4, column=3, sticky="nsew")
log_basee = Button(root, button_params, text='log\u2082',command=lambda:btn_click('log2(')).grid(row=4, column=4, sticky="nsew")

#--5th row--

left_par = Button(root, button_params, text='(',command=lambda:btn_click('(')).grid(row=5, column=0, sticky="nsew")
right_par = Button(root, button_params, text=')',command=lambda:btn_click(')')).grid(row=5, column=1, sticky="nsew")   
signs = Button(root, button_params, text='\u00B1',command=sign_chng).grid(row=5, column=2, sticky="nsew")
eulers_num = Button(root, button_params, text='e',command=lambda:btn_click(str(math.exp(1)))).grid(row=5, column=3, sticky="nsew")
ex = Button(root, button_params, text='e^x',command=lambda:btn_click('e(')).grid(row=5, column=4, sticky="nsew")

#--6th row--

button_7 = Button(root, button_params_main, text='7',command=lambda:btn_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(root, button_params_main, text='8',command=lambda:btn_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(root, button_params_main, text='9',command=lambda:btn_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(root, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='DEL', command=btn_dlt, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(root, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='AC', command=btn_clr, bg='#db701f').grid(row=6, column=4, sticky="nsew")

#--7th row--

button_4 = Button(root,button_params_main, text='4',command=lambda:btn_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(root,button_params_main, text='5',command=lambda:btn_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(root,button_params_main, text='6',command=lambda:btn_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(root, button_params_main, text='*',command=lambda:btn_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(root, button_params_main, text='/',command=lambda:btn_click('/')).grid(row=7, column=4, sticky="nsew")

#--8th row--

button_1 = Button(root, button_params_main, text='1',command=lambda:btn_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(root, button_params_main, text='2',command=lambda:btn_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(root, button_params_main, text='3',command=lambda:btn_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(root, button_params_main, text='+',command=lambda:btn_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(root, button_params_main, text='-',command=lambda:btn_click('-')).grid(row=8, column=4, sticky="nsew")

#--9th row--

button_0 = Button(root, button_params_main, text='0',command=lambda:btn_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(root, button_params_main, text='.',command=lambda:btn_click('.')).grid(row=9, column=1, sticky="nsew")
exp = Button(root,button_params_main,text='EXP',font=('sans-serif',16,'bold'),command=lambda:btn_click(E)).grid(row=9,column=2,sticky="nsew")
equal = Button(root, button_params_main, text='=',command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")

root.mainloop()