""" Tkinter is for the GUI. """
from tkinter import Tk, Label, Frame

W_WIDTH = 500
W_HEIGHT = 300

window = Tk()
window.geometry = str(W_WIDTH) + "x" + str(W_HEIGHT)
window.title("Application")

# This is where the list of tasks will go.
tasks_frame = Frame(background="#FFFFFF", width=W_WIDTH, height=W_HEIGHT)
tasks_frame.pack()

# This is where the buttons at the bottom will go.
buttons_frame = Frame(background="#D9D9D9")
buttons_frame.pack()

hello_label = Label(text="Hello World!")
hello_label.place(x=300, y=300)

window.mainloop()
