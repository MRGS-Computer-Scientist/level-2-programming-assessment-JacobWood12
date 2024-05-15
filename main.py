""" Tkinter is for the GUI. """
from tkinter import Tk, Label

window = Tk()
window.geometry = "300x300"
window.title("Application")

hello_label = Label(text="Hello World!")
hello_label.place(x=300, y=300)

window.mainloop()
