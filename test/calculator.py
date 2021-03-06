from Tkinter import *

root = Tk()
root.title("Calculator") #window title

#e is entry widget
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx =10 , pady = 10)

first_number = ""

def button_add():
	global math
	global first_number
	math = "addition"
	f_num = e.get()
	e.delete(0, END)
	first_number = f_num





def button_subtract():
	global math
	global first_number
	math = "subtraction"
	return
def button_multiply():
	global math
	global first_number
	math = "multiplication"
	return
def button_divide():
	global math
	global first_number
	math = "division"
	return

def button_clear():
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	if math == "addition":
		e.insert(0, float(first_number) + float(second_number))
	if math == "subtraction":
		e.insert(0, float(first_number) - float(second_number))
	if math == "multiplication":
		e.insert(0, float(first_number) * float(second_number))
	if math == "division":
		e.insert(0, float(first_number) / float(second_number))
	
def button_click(number):
	current = e.get() 
	e.delete(0, END)
	e.insert(0, str(current) + str(number))	
#button_click(1): 
	#current = e.get() #current = 1 
	# e.delete(0, END) 
	# e.insert(0, str(current) + str(number)) #put 1 is in entry box 
	# return;	
#button_click(2): 
	#current = e.get() current = 2
	# e.delete(0, END) #delete 1 in the entry box
	# e.insert(0, str(current) + str(number)) #put 12 is in textbox 
	# return;	


#Ways to pass parameters:
#I: e.get()
#button_1 = Button(root,command = button_click)

#def button_click(number):
	#current = e.get()

#II: lambda
#button_1 = Button(root,command = lambda:button_click(a))

#def button_click(a):


#define buttons
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))

button_add = Button(root, text = "+", padx = 39, pady = 20, command = button_add) 
button_subtract = Button(root, text = "-", padx = 39, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "*", padx = 39, pady = 20, command = button_multiply) 
button_divide = Button(root, text = "/", padx = 39, pady = 20, command = button_divide) 

button_equal = Button(root, text = "=", padx = 40, pady = 40, command = button_equal) 

button_clear = Button(root, text = "Clear", padx = 80, pady = 20, command = button_clear) 

# plus sign is a symbol, the width is a little different so padx= 39

#put buttons on the screen

button_7.grid(row= 1,column = 0)
button_8.grid(row= 1,column = 1)
button_9.grid(row= 1,column = 2)

button_4.grid(row= 2,column = 0)
button_5.grid(row= 2,column = 1)
button_6.grid(row= 2,column = 2)

button_1.grid(row= 3,column = 0)
button_2.grid(row= 3,column = 1)
button_3.grid(row= 3,column = 2)

button_0.grid(row= 4,column = 0)
button_clear.grid(row= 4, column= 1, columnspan = 2)

button_add.grid(row= 5, column= 0)
button_subtract.grid(row= 5, column= 1)
button_equal.grid(row= 5, column= 2, rowspan = 2)

button_multiply.grid(row= 6, column= 0)
button_divide.grid(row= 6, column= 1)

#default columnspan = 1
#columnspan = 2: we only see 1 button, but it's occupying 2 cells
#The column will default to the cell that will accomodate the widest item
#button_clear.grid(row= 4, column= 1) in this case, each cell i has the same size as the clear button since it's the largest.

root.mainloop()
