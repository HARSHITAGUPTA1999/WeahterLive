#organising the layout
from tkinter import *
#organising the layout (general)
root = Tk()
#frames: invisible containers
top_frame = Frame(root)
top_frame.pack(side=TOP)
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

#making widgets
button1 = Button(top_frame, text="button 1", fg="pink")
button2 = Button(top_frame, text="button 2", fg="maroon")
button3 = Button(top_frame, text="button 3", fg="blue")
button4 = Button(bottom_frame, text="button 4", fg="orange")

#displaying widgets
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()