#Answer 1
from tkinter import *
root=Tk()
hwl=Label(root,text="Hello World")
btn=Button(root,command=root.destroy,text="Exit")
hwl.pack()
btn.pack()
root.mainloop()
