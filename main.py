from tkinter import *
from PIL import Image, ImageTk

#-------------Main Window-------

#The first window is the main - where the user identifies as employer or employee 
mainWindow = Tk()
mainWindow.title("Salary Calculator: Easy Pay")
#mainWindow.geometry("500x500") - will change later
#mainWindow.configure(bg= "white")

#-------------Frames------------
#mainFrame1 (top)- where the all the text will go
#mainFrame2 (middle)- where the images will go
#mainFrame3 (bottom)- where the buttons will go


#My top frame
mainFrame1 = LabelFrame(mainWindow, padx= 10, pady= 10)
mainFrame1.grid(row = 0, column = 0, rowspan= 10, columnspan= 10)

#My middle frame
mainFrame2 = LabelFrame(mainWindow, padx= 10, pady= 10)
mainFrame2.grid(row= 10, column= 0, rowspan= 10, columnspan= 10)

#My bottom frame
mainFrame3 = LabelFrame(mainWindow, padx=10, pady=10)
mainFrame3.grid(row= 15, column= 0, rowspan= 10, columnspan= 10)

#--------Labels----------------
#Includes the app name and asks the user what are they (employer or employee)

nameLabel = Label(mainFrame1, text= "Salary Calculator")
nameLabel.grid(row= 0, column= 0)

nameLabel2 = Label(mainFrame1, text= "Easy Pay")
nameLabel2.grid(row = 2, column= 0)

whatAreYouLabel = Label(mainFrame1, text= "WHAT ARE YOU?")
whatAreYouLabel.grid(row = 5, column=0)

#----------pictures--------------
#This will go in mainFrame2

#-----need to resize them to make it look better/ make it fit
#Employer image icon
employerImage = ImageTk.PhotoImage(Image.open("employer.png"))
employerImageLabel = Label(mainFrame2, image= employerImage)
employerImageLabel.grid(row = 2, column= 0)

#Employee image icon
employeeImage = ImageTk.PhotoImage(Image.open("userImage.png"))
employeeImageLabel = Label(mainFrame2, image = employeeImage)
employeeImageLabel.grid(row = 2, column= 5)

#----------Buttons----------------
#These will go in mainFrame3

#Button that takes you to the second window
#Takes you to the employer window

employerButton = Button(mainFrame3, text = "Employer")
employerButton.grid(row = 0, column= 0)

#Button that takes you to the third window
#Takes you to the employee window

employeeButton = Button(mainFrame3, text = "Employee")
employeeButton.grid(row = 0, column= 5)


mainWindow.mainloop()