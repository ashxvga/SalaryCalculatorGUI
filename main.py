"""
This application will allow the user is to generate salaries wheter they are an employer or employee. 
-change later
"""
#My imports
from tkinter import *
from PIL import Image, ImageTk
import employerWindow
import employeeWindow
import helpWindow


#-------------Main Window-------

#The first window is the main - where the user identifies as employer or employee 
mainWindow = Tk()
mainWindow.title("Salary Calculator: Easy Pay")
#mainWindow.geometry("915x500") #- will change later



#-------------Frames for mainWindow------------
#mainFrame1 (top)- where the all the text will go
#mainFrame2 (middle)- where the images will go
#mainFrame3 (bottom)- where the buttons will go


#My top frame
mainFrame1 = Frame(mainWindow, padx= 50, pady= 10)
mainFrame1.grid(row = 0, column = 0, rowspan= 10, columnspan= 10)

#My middle frame
mainFrame2 = Frame(mainWindow, padx= 50, pady= 10)
mainFrame2.grid(row= 10, column= 0, rowspan= 10, columnspan= 10)

#My bottom frame
mainFrame3 = Frame(mainWindow, padx=50, pady=10)
mainFrame3.grid(row= 20, column= 0, rowspan= 10, columnspan= 10)

#--------Labels----------------
#Includes the app name and asks the user what are they (employer or employee)

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
employerImage = Image.open("key.png").resize((250,250))
employerImageTk = ImageTk.PhotoImage(employerImage)
employerImageLabel = Label(mainFrame2, image= employerImageTk, text="Employer Icon: Holding Key", compound="top")
employerImageLabel.image = employerImageTk
employerImageLabel.grid(row = 2, column= 0)

#Employee image icon
employeeImage = Image.open("person.png").resize((250,250))
employeeImageTk = ImageTk.PhotoImage(employeeImage)
employeeImageLabel = Label(mainFrame2, image = employeeImageTk, text="Employee Icon", compound="top")
employeeImageLabel.image = employeeImageTk
employeeImageLabel.grid(row = 2, column= 5)

#----------Buttons----------------
#These will go in mainFrame3

#Button that takes you to the second window
#Takes you to the employer window


employerButton = Button(mainFrame3, text = "Employer", command= lambda: openEmployer())
employerButton.grid(row = 0, column= 0)

#Button that takes you to the third window
#Takes you to the employee window

employeeButton = Button(mainFrame3, text = "Employee", command= lambda: openEmployee())
employeeButton.grid(row = 0, column= 3)

#Button that opens the fourth window
#Takes you to the help window
helpButton = Button(mainFrame3, text = "Help",command=helpWindow.open_help_window)
helpButton.grid(row = 0, column= 5)

#This will make sure to only allow the user to have one type of window open
#Meaning if the employer window is open, the employee window closes and viceversa

#This closes the employee window (if it's open) and opens the employer window
def openEmployer():
    if employeeWindow.employee_window is not None and employeeWindow.employee_window.winfo_exists():
        employeeWindow.employee_window.destroy() 
    employerWindow.openEmployerWindow(mainWindow)  

#This closes the employer window (if it's open) and opens the employee window
def openEmployee():
    if employerWindow.employer_window is not None and employerWindow.employer_window.winfo_exists():
        employerWindow.employer_window.destroy()
    employeeWindow.openEmployeeWindow(mainWindow) 



mainWindow.mainloop()
