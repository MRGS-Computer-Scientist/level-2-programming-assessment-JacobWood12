""" Tkinter is for the GUI. """
from tkinter import Tk, Frame, Button

def addtask():
    """ Add task function, activated when the "Add Task" button is pressed. """
    print("Add task button pressed!")

# Defines height and width of the window.
w_width = 500
w_height = 750

# Sets up window.
window = Tk()
window.geometry = str(w_width) + "x" + str(w_height)
window.title("Application")

# This is where the list of tasks will go.
tasks_frame = Frame(background="#FFFFFF", width=w_width, height=650)
tasks_frame.pack()

# This is where the buttons at the bottom will go.
buttons_frame = Frame(background="#D9D9D9", width=w_width, height=150)
buttons_frame.pack()

# Button that runs the addtask function.
addtask_button = Button(buttons_frame, text="+ | Add Task", command=addtask, bg="#D9D9D9")
addtask_button.place(relx=0.5, rely=0.5, anchor="center")

# Task button.
task_button = Button(tasks_frame, text="Task 1")
task_button.pack()

window.mainloop()
