""" Tkinter is for the GUI. """
from tkinter import Tk, Label, Frame

W_WIDTH = 300
W_HEIGHT = 300

window = Tk()
window.geometry = str(W_WIDTH) + "x" + str(W_HEIGHT)
window.title("Application")

main_frame = Frame(background="red", width=W_WIDTH, height=W_HEIGHT)
main_frame.pack()

hello_label = Label(text="Hello World!")
hello_label.place(x=300, y=300)

window.mainloop()
