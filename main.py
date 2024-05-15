""" Tkinter is for the GUI. """
from tkinter import Tk, Label

window = Tk()
window.geometry = "300x300"
window.title("Application")

# Defines layout manager as grid.
window.grid()

hello_label = Label(text="Hello World!")
hello_label.grid(column=0,row=0)

goodbye_label = Label(text="Goodbye World!")
goodbye_label.grid(column=1,row=1)

window.mainloop()
