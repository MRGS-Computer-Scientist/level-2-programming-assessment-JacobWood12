""" Tkinter is for the GUI. """
from tkinter import Tk, Label

W_WIDTH = 300
W_HEIGHT = 300

window = Tk()
window.geometry = W_WIDTH + W_HEIGHT
window.title("Application")

hello_label = Label(text="Hello World!")
hello_label.place(x=300, y=300)

window.mainloop()
