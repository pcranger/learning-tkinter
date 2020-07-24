from Tkinter import *

root = Tk()

#this label widget is going in our root widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "                  ")
myLabel3 = Label(root, text = "My name is Hieu")

#putting it onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
myLabel3.grid(row = 1, column = 3)



 #event loop
root.mainloop()
