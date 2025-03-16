from tkinter import *

root = Tk()

root.config(background="blue")
root.geometry("600x600")

#Labels
username = Label(root, text="Username").place(x=20, y=40)
password = Label(root, text="Password").place(x=20, y=90)

click = Button(root, text="Save", background="red")
click.place(x=52, y=150)
# click.pack(side="right")

username_entry = Entry(root, width=50, background="green", highlightcolor="white", highlightthickness="2").place(x=90, y=40)
password_entry = Entry(root, width=50, background="green", highlightcolor="white", highlightthickness="2").place(x=90, y=90)

#MenuBar
menu_bar = Menu(root)
file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="New File")
file.add_command(label="New Window")
file.add_command(label="Open")

edit = Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo")
edit.add_command(label="Redo")
root.config(menu=menu_bar)

#Spinbox
spin = Spinbox(root, from_=0, to=10)
spin.pack(side="bottom")


root.mainloop()