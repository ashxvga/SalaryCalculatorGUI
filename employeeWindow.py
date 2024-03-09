"""
This module defines the functionality for the employee window.
It allows the user to input their details such as name, worked hours, 
hourly salary, overtime rate, and tax rate, and calculates their 
salary based on these inputs. It also provides allows 
to clear the input fields and display help information.
"""

#My imports
from tkinter import *
import calculations
import helpWindow

#This will be my global variables
employee_window = None  # This will store the employee window
enterUserName = None  # This is the entry field for user name input (textbox)
enterWorkedHours = None  # This is the entry field for worked hours input (textbox)
enterHourlySalary = None  # This is the entry field for hourly salary input (textbox)
enterOvertimeRate = None  # This is the entry field for overtime rate input (textbox)
entertaxRate = None  # This is the entry field for tax rate input
result_label = None  # This is the label to display the calculation results

#This function will open the Employee Window
def openEmployeeWindow(mainWindow):
    global employee_window, enterUserName, enterWorkedHours, enterHourlySalary, enterOvertimeRate, entertaxRate, result_label
    
    #This will check if the window is already open
    #It will prevent having multiples of the same window
    #It destroys the already opened window
    if employee_window is not None and employee_window.winfo_exists():
        employee_window.destroy()

    #The new window
    employee_window = Toplevel(mainWindow)
    employee_window.title("Employee Window")

#-------------------frames----------------------------------
#secondFrame1 - where all the labels will go
#secondFrame2 - where all the texboxes will go
#secondFrame3 - where all the buttons will go
#secondFrame4 - where all info will be displayed
    
    #my secondFrame1
    secondFrame1 = Frame(employee_window, padx=10, pady=10)
    secondFrame1.grid(row=0, column=0, rowspan=10, columnspan=10)
    #my secondFrame2
    secondFrame2 = Frame(employee_window, padx=50, pady=10)
    secondFrame2.grid(row=10, column=0, rowspan=10, columnspan=10)
    #My secondFrame3
    secondFrame3 = Frame(employee_window, padx=50, pady=10)
    secondFrame3.grid(row=20, column=0, rowspan=10, columnspan=10)
    #My secondFrame4
    secondFrame4 = Frame(employee_window, padx=50, pady=10)
    secondFrame4.grid(row=30, column=0, rowspan=10, columnspan=10)
#--------------------Labels-----------------------------------
    
    nameLabel = Label(secondFrame1, text="Salary Calculator", fg="#FFD300", font=("Comic Sans MS", 35))
    nameLabel.grid(row=0, column=0)
    nameLabel2 = Label(secondFrame1, text="Easy Pay", fg="orange", font=("Comic Sans MS", 24))
    nameLabel2.grid(row=2, column=0)

    LABEL_WIDTH = 20 #This is a fixed width for the labels, it makes it easier to align them

    #Labels to asks the user the info
    userNameLabel = Label(secondFrame2, text="Your Name:", width=LABEL_WIDTH, anchor="w", justify="left")
    userNameLabel.grid(row=0, column=0)
    workedHoursLabel = Label(secondFrame2, text="Worked Hours:", width=LABEL_WIDTH, anchor="w", justify="left")
    workedHoursLabel.grid(row=1, column=0)
    hourlySalaryLabel = Label(secondFrame2, text="Hourly Salary:", width=LABEL_WIDTH, anchor="w", justify="left")
    hourlySalaryLabel.grid(row=2, column=0)
    overtimeRateLabel = Label(secondFrame2, text="Overtime Pay Rate(1.5 & over):", width=LABEL_WIDTH, anchor="w", justify="left")
    overtimeRateLabel.grid(row=3, column=0)
    taxRateLabel = Label(secondFrame2, text="Tax Rate (Ex: 3.4):", width=LABEL_WIDTH, anchor="w", justify="left")
    taxRateLabel.grid(row=4, column=0)

#----------------------Texbox-------------------
    #where the user will be able to input/enter the required info
    enterUserName = Entry(secondFrame2, width=10)
    enterUserName.grid(row=0, column=1)
    enterWorkedHours = Entry(secondFrame2, width=10)
    enterWorkedHours.grid(row=1, column=1)
    enterHourlySalary = Entry(secondFrame2, width=10)
    enterHourlySalary.grid(row=2, column=1)
    enterOvertimeRate = Entry(secondFrame2, width=10)
    enterOvertimeRate.grid(row=3, column=1)
    entertaxRate = Entry(secondFrame2, width=10)
    entertaxRate.grid(row=4, column=1)
#---------------------buttons-----------------------------------
    #takes you back to the main window
    exitButton = Button(secondFrame3, text="BACK/EXIT", command=lambda: back_to_main_window(employee_window))
    exitButton.grid(row=0, column=0)

    #This will delete the info entered in the textboxes
    deleteButton = Button(secondFrame3, text="DELETE", command=clear_entries)
    deleteButton.grid(row=0, column=1)

#where the results will be displayed
#It will take the text from the calculations.py module and display them here
    result_label = Label(secondFrame4, text="", font=("Arial", 14))
    result_label.grid(row=1, column=0)

#This function will retrieve input values, validate them, and calculate the salary
    def calculate_and_display():
        user_name = enterUserName.get().strip()#This gets the user's name + removes whitespaces
        worked_hours_str = enterWorkedHours.get().strip()#This gets the worked hours + removes whitespaces
        hourly_salary_str = enterHourlySalary.get().strip()#This gets the hourly salary  + removes ws.
        overtime_rate_str = enterOvertimeRate.get().strip()#This gets the overtime rate + removes ws.
        tax_rate_str = entertaxRate.get().strip()#This gets the tax rate + removes whitespaces
    
    #--- Here is the data validation--
        #This will check if any of the textboxes are empty
        #If one or more are empty, it will display an error
        if not all([user_name, worked_hours_str, hourly_salary_str, overtime_rate_str, tax_rate_str]):
            result_label.config(text="Please fill in all the fields.")
            return
        #This will check if the textbox for the name have numbers
        #If one or more have numbers, it will display an error
        if any(char.isdigit() for char in user_name):
            result_label.config(text="Names cannot contain numbers.")
            return
        
        #This will convert input strings to floats and 
        #it will also perform type conversion validation
        try:
            worked_hours = float(worked_hours_str)
            hourly_salary = float(hourly_salary_str)
            overtime_rate = float(overtime_rate_str)
            tax_rate = float(tax_rate_str)
        # If any input cannot be converted to float
        #this will display an error message
        except ValueError:
            result_label.config(text="Please enter valid numbers for worked hours, hourly salary, overtime rate, and tax rate.")
            return
        
        #What if the user enters a negative number?
        #This will check if any input value is negative
        #It will display an error message if there are negative nums
        if worked_hours < 0 or hourly_salary < 0 or overtime_rate < 0 or tax_rate < 0:
            result_label.config(text="Please enter positive values for worked hours, hourly salary, overtime rate, and tax rate.")
            return
        
        #In the U.S. the overtime rate must start at 1.5 
        #This will check if the overtime rate is less than 1.5, 
        #If it's lower, it will display an error message
        if overtime_rate < 1.5:
            result_label.config(text="Overtime tax rate must be equal to or greater than 1.5.")
            return
        
        #This will use the the calculations.py module to calculate the salary
        result = calculations.calculateAndDisplayEmployeeSalary(user_name, worked_hours, hourly_salary, overtime_rate, tax_rate)
        result_label.config(text=result)

    # This button will trigger the salary calculation function
    calculateButton = Button(secondFrame3, text="CALCULATE", command=calculate_and_display)
    calculateButton.grid(row=0, column=2)

    #this is the button to the help menu/window!
    helpButton = Button(secondFrame3, text="Help", command=helpWindow.open_help_window)
    helpButton.grid(row=0, column=5)

#This function will allows to return to the main window
#for the exit/back button
#it destroys the window
def back_to_main_window(window):
    window.destroy()

#This function will clear all entry fields (textboxes)
#it also resets the result label
#for the delete button
def clear_entries():
    enterUserName.delete(0, END)
    enterWorkedHours.delete(0, END)
    enterHourlySalary.delete(0, END)
    enterOvertimeRate.delete(0, END)
    entertaxRate.delete(0, END)
    result_label.config(text="")
