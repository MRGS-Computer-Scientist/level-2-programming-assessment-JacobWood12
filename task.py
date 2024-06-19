""" This is the task window that displays when each task button in the main window is clicked. """
# Tkinter is for the GUI.
from tkinter import Tk, Label
from app_settings import task_font

class Task():
	""" Contains the task window(s). """
	def __init__(self, instance):
		task_window = Tk()
		task_window.geometry = "200x200"

		task_label  = Label(task_window, text="Task " + str(instance), font=task_font)
		task_label.pack()

		task_window.mainloop()
