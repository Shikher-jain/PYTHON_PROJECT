# import required module
from tkinter import *


# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

	# adjusting backgroung of the widget
	# background on entering widget
	button.bind("<Enter>", func=lambda e: button.config(
		background=colorOnHover))

	# background color on leving widget
	button.bind("<Leave>", func=lambda e: button.config(
		background=colorOnLeave))


# Driver Code
root = Tk()

# create button
# assign button text along
# with background color
myButton = Button(root,
				text="On Hover - Background Change",
				bg="yellow")
myButton.grid()

# call function with background
# colors as argument
changeOnHover(myButton, "red", "yellow")

root.mainloop()
