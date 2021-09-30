from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Autoscript 3")
root.geometry("1000x1000")

anchorOne = "anchor 1"
anchorTwo = "anchor 2"

#Define Labels
anchorOne_LABEL = Label(root, text=anchorOne)
anchorTwo_LABEL = Label(root, text=anchorTwo)

#Define Entries
anchorOne_ENTRY = Entry(root)
anchorTwo_ENTRY = Entry(root)

#Define Buttons

#Define Menu
main_MENU = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')

file = Menu(main_MENU, tearoff=0) 
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Print")
file.add_separator()  
file.add_command(label="Quit", command=root.quit)  
main_MENU.add_cascade(label="File", menu=file)  

edit = Menu(main_MENU, tearoff=0)  
edit.add_command(label="Add Announcement")
edit.add_command(label="Delete Announcement")
edit.add_separator()  
edit.add_command(label="Preferences")
edit.add_command(label="Configuration")
main_MENU.add_cascade(label="Edit", menu=edit)  

help = Menu(main_MENU, tearoff=0)
help.add_command(label="About")
main_MENU.add_cascade(label="Help", menu=help)  

#Set default Menu
root.config(menu=main_MENU)

#Define Frames
left_FRAME = LabelFrame(root, text="Announcements")
left_FRAME.pack(side="left")

center_FRAME = LabelFrame(root)
center_FRAME.pack(side="top")

right_FRAME = LabelFrame(root, text="Information")
right_FRAME.pack(side="right")

#Pack everything
anchorOne_LABEL.pack()
anchorTwo_LABEL.pack()

root.mainloop()