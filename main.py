"""
This application will allow the user to generate salaries whether they are an employer or employee. 
-change later
"""
from tkinter import *
from PIL import Image, ImageTk
import openWindows

#-------------Main Window-------

#The first window is the main - where the user identifies as an employer or employee 
mainWindow = Tk()
mainWindow.title("Salary Calculator: Easy Pay")
#mainWindow.geometry("500x500") - will change later



#-------------Frames for mainWindow------------
#mainFrame1 (top)- where all the text will go
#mainFrame2 (middle)- where the images will go
#mainFrame3 (bottom)- where the buttons will go


#My top frame
mainFrame1 = LabelFrame(mainWindow, padx= 312, pady= 10)
mainFrame1.grid(row = 0, column = 0, rowspan= 10, columnspan= 10)

#My middle frame
mainFrame2 = LabelFrame(mainWindow, padx= 200, pady= 10)
mainFrame2.grid(row= 10, column= 0, rowspan= 10, columnspan= 10)

#My bottom frame
mainFrame3 = LabelFrame(mainWindow, padx=360, pady=10)
mainFrame3.grid(row= 30, column= 0, rowspan= 10, columnspan= 10)

#--------Labels----------------
#Includes the app name and asks the user what they are (employer or employee)

nameLabel = Label(mainFrame1, text= "Salary Calculator", fg = "#FFD300", font =("Comic Sans MS",35))
nameLabel.grid(row= 0, column= 0)

nameLabel2 = Label(mainFrame1, text= "Easy Pay", fg = "orange", font = ("Comic Sans MS",24))
nameLabel2.grid(row = 2, column= 0)

whatAreYouLabel = Label(mainFrame1, text= "WHAT ARE YOU?", font = ("Comic Sans MS", 30))
whatAreYouLabel.grid(row = 10, column=0)

#----------pictures--------------
#This will go in mainFrame2

#-----need to resize them to make it look better/ make it fit
#Employer image icon
employerImage = ImageTk.PhotoImage(Image.open("key.png").resize((250,250)))
employerImageLabel = Label(mainFrame2, image= employerImage)
employerImageLabel.grid(row = 2, column= 0)

#Employee image icon
employeeImage = ImageTk.PhotoImage(Image.open("person.png").resize((250,250)))
employeeImageLabel = Label(mainFrame2, image = employeeImage)
employeeImageLabel.grid(row = 2, column= 5)

#----------Buttons----------------
#These will go in mainFrame3

#Button that takes you to the second window
#Takes you to the employer window

employerButton = Button(mainFrame3, text = "Employer", command= lambda: openWindows.openEmployerWindow(mainWindow))
employerButton.grid(row = 0, column= 0)

#Button that takes you to the third window
#Takes you to the employee window

employeeButton = Button(mainFrame3, text = "Employee", command= lambda: openWindows.openEmployeeWindow(mainWindow))
employeeButton.grid(row = 0, column= 5)


"""
#doesn't work
#---------Frames for second window
#trial #1
secondWindow = openWindows.openEmployerWindow(mainWindow)
secondFrame1 = LabelFrame(secondWindow, padx= 312, pady= 10)
secondFrame1.grid(row = 0, column = 0, rowspan= 10, columnspan= 10)
SecondNameLabel = Label(secondFrame1, text= "Your Name", fg = "#FFD300", font =("Arial",12))
SecondNameLabel.grid(row= 0, column= 0)

#trial #2
#My top frame
secondFrame1 = LabelFrame(secondWindow, padx= 312, pady= 10)
secondFrame1.grid(row = 0, column = 0, rowspan= 10, columnspan= 10)

#doesn't work either

#My middle frame
secondFrame2 = LabelFrame(openWindows.openEmployerWindow(mainWindow), padx= 200, pady= 10)
secondFrame2.grid(row= 10, column= 0, rowspan= 10, columnspan= 10)

#My bottom frame
secondFrame3 = LabelFrame(openWindows.openEmployerWindow(secondWindow), padx=360, pady=10)
secondFrame3.grid(row= 30, column= 0, rowspan= 10, columnspan= 10)

SecondNameLabel = Label(secondFrame1, text= "Your Name", fg = "#FFD300", font =("Arial",12))
SecondNameLabel.grid(row= 0, column= 0)
"""

mainWindow.mainloop()

employeeButton = Button(mainFrame3, text = "Employee")
employeeButton.grid(row = 0, column= 5)


mainWindow.mainloop()
