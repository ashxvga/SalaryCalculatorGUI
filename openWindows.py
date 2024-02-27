from tkinter import *


def openEmployerWindow(mainWindow):
  secondWindow = Toplevel(mainWindow) #associates it to the main window
  secondWindow.title("Employer Window")
  label = Label(secondWindow, text = "This is the second window")
  label.grid(row = 0, column = 0, rowspan= 10, columnspan = 2)

def openEmployeeWindow(mainWindow):
  thirdWindow = Toplevel(mainWindow) #associates it to the main window
  thirdWindow.title("Employee Window")
  label = Label(thirdWindow, text = "This is the third window")
  label.grid(row = 0, column = 0, rowspan= 10, columnspan = 2)

  