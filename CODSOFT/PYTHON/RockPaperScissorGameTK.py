from tkinter import *
import random
from PIL import Image,ImageTk

usr_scr = 0
bot_scr = 0
options = [('  rock  ',0), ('  paper ',1), ('scissors',2)]

def usr_ch(usr_IP):
    global usr_scr, bot_scr
    computer_input = random.choice(options)
    user_ch_lbl.config(text = 'Your Selected : ' + usr_IP[0])
    bot_ch_lbl.config(text = 'Computer Selected : ' + computer_input[0])

    if(usr_IP == computer_input):
        winner_lbl.config(text = "Tie")
    elif((usr_IP[1] - computer_input[1]) % 3 == 1):
        usr_scr += 1
        winner_lbl.config(text="You Won!!!")
        user_scr_lbl.config(text = 'Your Score : ' + str(usr_scr))
    else:
        bot_scr += 1
        winner_lbl.config(text="Computer Won!!!")
        bot_scr_lbl.config(text='Your Score : ' + str(bot_scr))

root = Tk()
root.title("Rock Paper Scissors Game")
root.config(bg="white")

app_font = "times 20 bold"
scr_font = "times 15 bold"

Img1=Image.open("Shikher-jain/CODSOFT/PYTHON/Rock.jpg")
rockImg=ImageTk.PhotoImage(Img1)

Img2=Image.open("Shikher-jain/CODSOFT/PYTHON/Paper.jpg")
paperImg=ImageTk.PhotoImage(Img2)

Img3=Image.open("Shikher-jain/CODSOFT/PYTHON/Scissor.jpg")
scissorImg=ImageTk.PhotoImage(Img3)

game_title = Label(root,text = 'Rock Paper Scissors',bg="white", font="Times 40 italic bold", fg = 'red')
game_title.pack()

winner_lbl = Label(text = "Let's Start the Game...", fg = 'green',bg="white", font="times 25 bold", pady = 8 )
winner_lbl.pack()

F = Frame(root)
F.pack()

usr_opt = Label(F, text = "Your Options : ",font = app_font,bg="white", fg = 'blue')
usr_opt.grid(row = 0, column = 1, pady = 8)

rock_btn = Button(F,image=rockImg, bd = 0, bg = 'pink', pady = 5, command = lambda: usr_ch(options[0]))
rock_btn.grid(row = 1, column = 0, padx = 8, pady = 5)

paper_btn = Button(F,image=paperImg,bd = 0, bg = '#BA90C2', pady = 5, command = lambda: usr_ch(options[1]))
paper_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

scissors_btn = Button(F, image=scissorImg, bd = 0, bg = 'light blue', pady = 5, command = lambda: usr_ch(options[2]))
scissors_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

F1=Frame(root,bg="white")
F1.pack()
scr_lbl = Label(F, text = 'Score : ', font = app_font,bg="white", fg = 'yellow')

user_ch_lbl = Label(F1, text= 'Your Selected  : ---', justify="left",bg="white",font = scr_font)
user_scr_lbl = Label(F1, text = 'Your Score : -',bg="white", font = scr_font)
bot_ch_lbl = Label(F1, text = 'Computer Selected : ---',justify="left",bg="white", font = scr_font, fg = 'black')
bot_scr_lbl = Label(F1, text = 'Computer Score : -',bg="white", font = scr_font, fg = 'black')

scr_lbl.grid(row = 2, column = 1)

user_ch_lbl.grid (row = 3, column = 0,padx=(5,0))
user_scr_lbl.grid(row = 3, column = 1,padx=(5,0))
bot_ch_lbl.grid  (row = 4, column = 0,padx=(5,0))
bot_scr_lbl.grid (row = 4, column = 1,padx=(5,0))

root.resizable(width=False,height=False)
F.config(bg="white")
F1.config(bg="white")
root.mainloop()
