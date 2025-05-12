'''
import tkinter
from PIL import Image, ImageTk
# from PIL import *
import random

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Hello This Is Dice Game!!", fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
l1.pack()

# images
dice = ['die1.PNG', 
        'die2.PNG', 
        'die3.PNG', 
        'die4.PNG', 
        'die5.PNG', 
        'die6.PNG']
print(random.choice(dice))
# img=Image.open("die6.PNG")
# img.show()
print(Image.open("die6.PNG"))

# print(Image.open(random.choice(dice)))
# Image.open(random.choice(dice))
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1

# packing a widget in the parent widget 
label1.pack( expand=True)

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()

'''

import tkinter
from PIL import Image, ImageTk
import random
import os

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# Adding label into the frame
label_message = tkinter.Label(root, text="Hello! This is a Dice Game!!", fg="white",
                               bg="red",font="Helvetica 16 bold italic")
label_message.pack()

# Shikher-jain\PROJECTs\dice_images\die5.PNG

# Directory containing dice images
image_dir = "Shikher-jain/PROJECTs/dice_images/"
# List of dice images
dice = ['die1.PNG',
        'die2.PNG',
        'die3.PNG',
        'die4.PNG',
        'die5.PNG',
        'die6.PNG'
        ]

# Function to load a random dice image
def load_random_dice_image():
    image_path = os.path.join(image_dir, random.choice(dice))
    image = Image.open(image_path)
    return ImageTk.PhotoImage(image)
    # print(image_path)

# Initial image
image1 = load_random_dice_image()

# Construct a label widget for the image
label1 = tkinter.Label(root,image = image1)
label1.image = image1 # type: ignore
label1.pack(expand=True)

# Function activated by button to roll the dice
def rolling_dice():
    new_image = load_random_dice_image()
    label1.configure(image=new_image)
    label1.image = new_image # type: ignore

# # Button to roll the dice
button_roll_dice = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
button_roll_dice.pack(expand=True)

# Call the main loop of Tk
root.mainloop()
