from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageTk

root=Tk()

root.title("SHIKHER")

# witdth x height
root.geometry("600x600")

# witdth , height
# root.minsize(300,300)
# root.maxsize(900,900)

'''
    text = adds text
    bg = background
    fg = foreground
    font = sets of font
    1 -> font=("comicsansms",20,BOLD)
    1 -> font="comicsansms 20 bold"
    padx = x padding
    pady = y padding
    relief = border styling -> SUNKEN, RAISED, GROOVE, RIDGE
'''


l1=Label(text="This is Sample text" , bg="red",fg="pink",bd=12,padx=32,pady=52,font="comicsansms 20 bold",borderwidth=3,relief=SUNKEN)
# l1.pack()
attribute_of_pack_anchor=["n", "ne", "e", "se", "s", "sw", "w", "nw", "center"]
attribute_of_pack_side=[TOP,LEFT,BOTTOM,RIGHT]
for j in attribute_of_pack_side:
    for i in attribute_of_pack_anchor:
        l1_2=Label(text="This is Sample text" , bg="red",fg="pink",bd=12,padx=2,pady=2,font="comicsansms 20 bold",borderwidth=3,relief=SUNKEN)
        # l1_2.pack(side=j,anchor=i)
attribute_of_pack_fill=['none', 'x', 'y','both']
for k in attribute_of_pack_fill:
    l1_3=Label(text="This is Sample text" , bg="red",fg="pink",bd=12,padx=32,pady=52,font="comicsansms 20 bold",borderwidth=3,relief=SUNKEN)
    # l1_3.pack(fill=k)
l1_4=Label(text="This is Sample text" , bg="red",fg="pink",bd=12,padx=32,pady=52,font="comicsansms 20 bold",borderwidth=6,relief=SUNKEN)
l1_4.pack(side=LEFT,fill=Y,padx=20,pady=20)


# For png Images only
pic1=PhotoImage(file="Shikher-jain\TKINTER\dice.png")
pic_l2=Label(image=pic1)
# pic_l2.pack()

# For both png and jpg Images
pic_jpg=Image.open("Shikher-jain\TKINTER\cat.jpg")
pic2=ImageTk.PhotoImage(pic_jpg)
pic_l3=Label(image=pic2)
# pic_l3.pack()


l2=Button(text="IMAGE",bd=12,relief="flat",bg="blue",fg="white")
# l2.pack()


root.mainloop()