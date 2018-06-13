#Answer 4
from tkinter import *

def display():
	global lbl
	lbl.configure(text=namE.get())

root=Tk()
nam=Label(root,text="Enter your name")
namE=Entry(root)
btn=Button(root,text="Submit",command=display)
lbl=Label(root)
nam.pack()
namE.pack()
btn.pack()
lbl.pack()
root.mainloop()