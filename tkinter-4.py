from tkinter import *
class Buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="welcome", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quit = Button(frame, text="exit", command=frame.quit)
        self.quit.pack(side=LEFT)

    def printMessage(self):
        print("Today was a great day ")

#for drop down menu/toolbar  see ss
root = Tk()
b = Buttons(root)
root.mainloop()