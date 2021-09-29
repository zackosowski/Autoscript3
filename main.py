from tkinter import *
from tkinter import ttk

root = Tk()

anchorOne = "anchor 1"
anchorTwo = "anchor 2"

anchorOne_LABEL = Label(root, text=anchorOne)
anchorTwo_LABEL = Label(root, text=anchorTwo)

anchorOne_ENTRY = Entry(root)
anchorTwo_ENTRY = Entry(root)

anchorOne_LABEL.pack()
anchorTwo_LABEL.pack()

root.mainloop()