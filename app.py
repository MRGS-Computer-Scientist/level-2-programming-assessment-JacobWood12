""" The app class. """
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
	""" Contains the main window for now. """
	def __init__(self):
		# Sets up start screen.
		self.window = Tk()
		self.window.geometry = str(w_width) + "x" + str(w_height)
		self.window.title(window_title)

		# This is the frame where the list of tasks will go.
		self.tasks_frame = Frame(background=tasks_bg_colour, width=w_width, height=650)
		self.tasks_frame.grid()

		# This is the frame where the buttons at the bottom will go.
		self.buttons_frame = Frame(background=buttons_bg_colour, width=w_width, height=150)
		self.buttons_frame.grid()

		# Button that runs the addtask function.
		self.addtask_button = Button(self.buttons_frame, text="+ | Add Task", command=addtask, bg=buttons_bg_colour)
		self.addtask_button.place(relx=0.25, rely=0.5, anchor="center")

		# Button that closes the window.
		self.exit_button = Button(self.buttons_frame, text="Exit", command=exit, bg=buttons_bg_colour)
		self.exit_button.place(relx=0.75, rely=0.5, anchor="center")

		# Task buttons.
		self.task_button1 = Button(self.tasks_frame, text="Task 1", command= lambda: task_button_pressed(1))
		self.task_button1.grid(row=0,column=0)

		self.task_button2 = Button(self.tasks_frame, text="Task 2", command= lambda: task_button_pressed(2))
		self.task_button2.grid(row=1,column=0)

		self.task_button3 = Button(self.tasks_frame, text="Task 3", command= lambda: task_button_pressed(3))
		self.task_button3.grid(row=2,column=0)

		self.task_button4 = Button(self.tasks_frame, text="Task 4", command= lambda: task_button_pressed(4))
		self.task_button4.grid(row=3,column=0)

		# Starts the program looping to open the window.
		self.window.mainloop()
