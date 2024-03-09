"""
This module gives functionality to the employer window.
It provides a window where the employer can input their details, 
including their name, employee's name, worked hours, hourly salary,
overtime rate, and tax rate. It calculates the salary based on the info
collected and displays the result. The window also offers
options to clear the texboxes, close the window, and access help information.

-Almost the same as the Employee window
"""

#my imports
from tkinter import *
import calculations
import helpWindow

employer_window = None #my global variable to store the employer window

#This function will open the Employer Window
def openEmployerWindow(mainWindow):
    global employer_window

    #This will check if the window is already open
    #It will prevent having multiples of the same window
    #It destroys the already opened window
    if employer_window is not None and employer_window.winfo_exists():
        employer_window.destroy()

#my new window
    employer_window = Toplevel(mainWindow)
    employer_window.title("Employer Window")
#-------------------frames----------------------------------
#secondFrame1 - where all the labels will go
#secondFrame2 - where all the texboxes will go
#secondFrame3 - where all the buttons will go
#secondFrame4 - where all info will be displayed
    
    #my secondFrame1
    secondFrame1 = Frame(employer_window, padx=10, pady=10)
    secondFrame1.grid(row=0, column=0, rowspan=10, columnspan=10)
    #my secondFrame2
    secondFrame2 = Frame(employer_window, padx=50, pady=10)
    secondFrame2.grid(row=10, column=0, rowspan=10, columnspan=10)

    #my secondFrame3
    secondFrame3 = Frame(employer_window, padx=50, pady=10)
    secondFrame3.grid(row=20, column=0, rowspan=10, columnspan=10)
    #my secondFrame4
    secondFrame4 = Frame(employer_window, padx=50, pady=10)
    secondFrame4.grid(row=30, column=0, rowspan=10, columnspan=10)

#--------------------Labels-----------------------------------
    nameLabel = Label(secondFrame1, text="Salary Calculator", fg="#FFD300", font=("Comic Sans MS", 35))
    nameLabel.grid(row=0, column=0)
    nameLabel2 = Label(secondFrame1, text="Easy Pay", fg="orange", font=("Comic Sans MS", 24))
    nameLabel2.grid(row=2, column=0)

    LABEL_WIDTH = 20#This is a fixed width for the labels, it makes it easier to align them

    #Labels to asks the user the info
    employerNameLabel = Label(secondFrame2, text="Your Name:", width=LABEL_WIDTH, anchor="w", justify="left")
    employerNameLabel.grid(row=0, column=0)
    employeeNameLabel = Label(secondFrame2, text="Employee Name:", width=LABEL_WIDTH, anchor="w", justify="left")
    employeeNameLabel.grid(row=1, column=0)
    workedHoursLabel = Label(secondFrame2, text="Worked Hours by Employee:", width=LABEL_WIDTH, anchor="w", justify="left")
    workedHoursLabel.grid(row=2, column=0)
    hourlySalaryLabel = Label(secondFrame2, text="Hourly Salary:", width=LABEL_WIDTH, anchor="w", justify="left")
    hourlySalaryLabel.grid(row=3, column=0)
    overtimeRateLabel = Label(secondFrame2, text="Overtime Pay Rate(1.5 & over):", width=LABEL_WIDTH, anchor="w", justify="left")
    overtimeRateLabel.grid(row=4, column=0)
    taxRateLabel = Label(secondFrame2, text="Tax Rate (Ex: 3.4):", width=LABEL_WIDTH, anchor="w", justify="left")
    taxRateLabel.grid(row=5, column=0)


#----------------------Texbox-------------------
    #where the user will be able to input/enter the required info
    enterEmployerName = Entry(secondFrame2, width=10)
    enterEmployerName.grid(row=0, column=1)
    enterEmployeeName = Entry(secondFrame2, width=10)
    enterEmployeeName.grid(row=1, column=1)
    enterWorkedHours = Entry(secondFrame2, width=10)
    enterWorkedHours.grid(row=2, column=1)
    enterHourlySalary = Entry(secondFrame2, width=10)
    enterHourlySalary.grid(row=3, column=1)
    enterOvertimeRate = Entry(secondFrame2, width=10)
    enterOvertimeRate.grid(row=4, column=1)
    entertaxRate = Entry(secondFrame2, width=10)
    entertaxRate.grid(row=5, column=1)

#---------------------buttons-----------------------------------
    #takes you back to the main window
    exitButton = Button(secondFrame3, text="BACK/EXIT", command=closeEmployerWindow)
    exitButton.grid(row=0, column=0)

#This will delete the info entered in the textboxes
    deleteButton = Button(secondFrame3, text="DELETE", command=lambda: clear_entries(enterEmployerName, enterEmployeeName, enterWorkedHours, enterHourlySalary, enterOvertimeRate, entertaxRate, result_label))
    deleteButton.grid(row=0, column=1)

#where the results will be displayed
#It will take the text from the calculations.py module and display them here
    result_label = Label(secondFrame4, text="", font=("Arial", 14))
    result_label.grid(row=1, column=0)

#This function will retrieve input values, validate them, and calculate the salary
    def calculate_and_display():
        try:
            #all of these will etrieve data from entry widgets
            yourName = enterEmployerName.get().strip()
            employeeName = enterEmployeeName.get().strip()
            workedHours_str = enterWorkedHours.get().strip()
            hourlySalary_str = enterHourlySalary.get().strip()
            overtimeRate_str = enterOvertimeRate.get().strip()
            taxRate_str = entertaxRate.get().strip()
            
            # Check if any of the entries are empty
            if not all([yourName, employeeName, workedHours_str, hourlySalary_str, overtimeRate_str, taxRate_str]):
                raise ValueError("Please fill in all the fields.")

            # Validates names, checks if there are only letters
            if any(char.isdigit() for char in yourName) or any(char.isdigit() for char in employeeName):
                raise ValueError("Names cannot contain numbers.")

            #This will convert to floats after validation
            try:
                workedHours = float(workedHours_str)
                hourlySalary = float(hourlySalary_str)
                overtimeRate = float(overtimeRate_str)
                taxRate = float(taxRate_str)
            except ValueError:
                raise ValueError("Please enter valid numbers for worked hours, hourly salary, overtime rate, and tax rate.")

            # Perform input validation for numeric fields
            if workedHours < 0 or hourlySalary < 0 or overtimeRate < 0 or taxRate < 0:
                raise ValueError("Negative values are not allowed.")
            
            # Additional input validation for overtime tax rate
            if overtimeRate < 1.5:
                raise ValueError("Overtime tax rate must be equal to or greater than 1.5.")

            # Call the calculation function and display the result
            result = calculations.calculateAndDisplaySalary(yourName, employeeName, workedHours, hourlySalary, overtimeRate, taxRate)
            result_label.config(text=result)

#This will help prevent bugs / errors while displaying.
#It will display what error is happening.
        except ValueError as e:
            result_label.config(text=str(e))

        except Exception as e:
            result_label.config(text=str(e))
    #This button will trigger the salary calculation function
    calculateButton = Button(secondFrame3, text="CALCULATE", command=calculate_and_display)
    calculateButton.grid(row=0, column=2)

    #this is the button to the help menu
    helpButton = Button(secondFrame3, text="Help", command=helpWindow.open_help_window)
    helpButton.grid(row=0, column=5)

#This function will allows to return to the main window
#for the exit/back button
#it destroys the window
def closeEmployerWindow():
    if employer_window is not None and employer_window.winfo_exists():
        employer_window.destroy()

#This function will clear all entry fields (textboxes)
#it also resets the result label
#for the delete button
def clear_entries(enterEmployerName, enterEmployeeName, enterWorkedHours, enterHourlySalary, enterOvertimeRate, entertaxRate, result_label):
    enterEmployerName.delete(0, END)
    enterEmployeeName.delete(0, END)
    enterWorkedHours.delete(0, END)
    enterHourlySalary.delete(0, END)
    enterOvertimeRate.delete(0, END)
    entertaxRate.delete(0, END)
    result_label.config(text="")

