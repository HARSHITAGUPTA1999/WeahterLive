from tkinter import *
root = Tk()
#using grid to organise widgets on screen
label1 = Label(root, text="Name", bg="yellow")
#label1.pack()
label2 = Label(root, text="Password", bg="pink")
#label2.pack()
#Entry() is used for user input.creates a blank input for user to enter stuff
entry1 = Entry(root)
entry2 = Entry(root)
#sticky parameter used to align the widget(N,S,E,W)
label1.grid(row=0, column=0, sticky=W)
label2.grid(row=1, column=0, sticky=W)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

#adding a checkbox
ch = Checkbutton(root, text="Keep me signed in")
#columnspan helps to span over more than 1 column
ch.grid( columnspan=2)

#how to make gui interact with computer(binding using functions)
def printname():
    print("Hi there.Its wednesday today")
#command parameter calls the function specified when clicked
button1 = Button(root, text="print", command=printname)
button1.grid(row=4, column=3)

#another technique for binding function to widget
#event is anything user does(eg, scroll,left click, right click)
def printhello(event):
    print("hello user.Have a good day!")
button2 = Button(root, text="new_print")
#bind function binds the widget.Button-1 is the name convention for left click.
button2.bind("<Button-1>", printhello)
button2.grid(row=4, column=5)

 

root.mainloop()