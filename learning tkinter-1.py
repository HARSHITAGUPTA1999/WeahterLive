from tkinter import *
# making a basic window

#blank window created( whenever see root--think of blank window)
root = Tk()
label_1 = Label(root, text="first program", bg='pink', fg='green')
# pack means just place it in the first place it is.
label_1.pack()
label_2 = Label(root, text="first program", bg='yellow', fg='blue')
# fill parameter means widget size grows was window size increases
label_2.pack(side=LEFT, fill=Y)

# mainloop loops your code infinite so the window is present on screen consistently
root.mainloop()



