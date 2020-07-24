from Tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text = "lmao")
	myLabel.pack()

myButton = Button(root, text = "Click me!", 
#state = DISABLED, 
#padx = 50,
command = myClick)
myButton.pack()
root.mainloop()