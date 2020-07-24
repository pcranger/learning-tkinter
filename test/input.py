from Tkinter import *

root = Tk()

e = Entry(root, width = 50, 
	#fg = 'red'
	)
e.pack()
e.insert(0, "Enter you Name: ") #text-hint
def myClick():
	hello = "hello" + e.get()

	myLabel = Label(root, text =hello)
	myLabel.pack()

myButton = Button(root, text = "Enter your name", 
#state = DISABLED, 
#padx = 50,
command = myClick)
myButton.pack()
root.mainloop()