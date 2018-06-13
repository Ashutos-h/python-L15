#Answer 3
from tkinter import *

def display():
	global hwl
	hwl.configure(text="Bye World")

root=Tk()
frame=Frame(root,bg="blue")
frame.pack()
hwl=Label(frame,text="Hi World")
hwl.pack()
btnE=Button(frame,text="Exit",command=root.destroy)
btnC=Button(frame,text="Change text",command=display)
btnE.pack(side="left")
btnC.pack(side="right")
root.mainloop()
