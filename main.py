""" Tkinter is for the GUI. """
from tkinter import Tk, Label, Frame

# Defines height and width of the window
w_width = 500
w_height = 300

# Sets up window.
window = Tk()
window.geometry = str(w_width) + "x" + str(w_height)
window.title("Application")

# This is where the list of tasks will go.
tasks_frame = Frame(background="#FFFFFF", width=w_width, height=w_height)
tasks_frame.pack()

# This is where the buttons at the bottom will go.
buttons_frame = Frame(background="#D9D9D9")
buttons_frame.pack()

# Sets up label.
hello_label = Label(text="Hello World!")
hello_label.place(x=300, y=300)

window.mainloop()
