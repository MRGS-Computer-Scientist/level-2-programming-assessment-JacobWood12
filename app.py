""" The app class of a GUI homework planner. """
# Tkinter is for the GUI, app_settings contains all the global variables.
from tkinter import Tk, Frame, Button
from app_settings import w_width, w_height, window_title, tasks_bg_colour, buttons_bg_colour

def addtask():
    """ Add task function, activated when the "Add Task" button is pressed. """
    print("Add task button pressed!")

def task_button_pressed(instance):
    """ Activated when one of the task buttons is pressed. """
    print(f"Task button {instance} pressed!")

class App:
    """ App. """
    def __init__(self):
        # Sets up window.
        window = Tk()
        window.geometry = str(w_width) + "x" + str(w_height)
        window.title(window_title)

        # This is where the list of tasks will go.
        tasks_frame = Frame(background=tasks_bg_colour, width=w_width, height=650)
        tasks_frame.grid()

        # This is where the buttons at the bottom will go.
        buttons_frame = Frame(background=buttons_bg_colour, width=w_width, height=150)
        buttons_frame.grid()

        # Button that runs the addtask function.
        addtask_button = Button(buttons_frame, text="+ | Add Task", command=addtask, bg=buttons_bg_colour)
        addtask_button.place(relx=0.5, rely=0.5, anchor="center")

        # Task button.
        task_button1 = Button(tasks_frame, text="Task 1", command= lambda: task_button_pressed(1))
        task_button1.grid(row=0,column=0)

        task_button2 = Button(tasks_frame, text="Task 2", command= lambda: task_button_pressed(2))
        task_button2.grid(row=1,column=0)

        task_button3 = Button(tasks_frame, text="Task 3", command= lambda: task_button_pressed(3))
        task_button3.grid(row=2,column=0)

        task_button4 = Button(tasks_frame, text="Task 4", command= lambda: task_button_pressed(4))
        task_button4.grid(row=3,column=0)

        window.mainloop()
