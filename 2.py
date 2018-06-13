#Answer 2
from tkinter import *


def display():
	global hwl
	hwl.configure(text="hello User")
root=Tk()
hwl=Label(root)
btn=Button(root,text="Press", command=display)
hwl.pack()
btn.pack()
root.mainloop()

