"""
The purpose of this module is to provide help and guidance
to the user. It imports necessary modules from tkinter 
and defines functions to create and manage the help window for the application.
"""

#my imports
from tkinter import *
from tkinter import ttk

# This will be a global variable to track whether help window is open or not
help_window_open = False
helpWindow = None

#This function will open the help window
def open_help_window():
    global help_window_open
    global helpWindow

    # If the help window is already open
    #it will do nothing
    if help_window_open:
        return

    help_window_open = True

    helpWindow = Toplevel()
    helpWindow.title("Help Window")
    helpWindow.geometry("500x500")

    # This will ensure the help window is always on top.
    # Will prevent it from getting lost between the other windows.
    helpWindow.attributes('-topmost', True)

    # --------------Canvas, Frames, Scroolbar for Second Window------------
    # mainBigFrame - frame containing the canvas and the other frames
    # myCanvas - where everything will go
    #helpFrame1 - where all the labels will go

    # My main frame
    mainBigFrame = Frame(helpWindow)
    mainBigFrame.pack(fill=BOTH, expand=1, side=LEFT)  # Pack to the left side

    # my canvas
    myCanvas = Canvas(mainBigFrame)
    myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

    # my scrollball
    myScrollBar = ttk.Scrollbar(mainBigFrame, orient=VERTICAL, command=myCanvas.yview)
    myScrollBar.pack(side=RIGHT, fill=Y)

    # Here I will configure the canvas
    myCanvas.configure(yscrollcommand=myScrollBar.set)
    # bounding the canvas
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))

    #My frame
    helpFrame1 = Frame(myCanvas)
    #Adding helpFrame1 to a window in the canvas
    myCanvas.create_window((0, 0), window=helpFrame1, anchor="nw")

    #Adding the instructions labels 
    tipLabel = Label(helpFrame1, text="""Tip: Drag this window to a convenient location to view instructions while using
other windows. Do NOT use the "X" button to close this 
window, use the "Close" button at the bottom of the window.""", width=70, anchor="w", justify="left")
    tipLabel.grid(row=0, column=0)
    disclaimerLabel = Label(helpFrame1, text="""Disclaimer: This calculator should only be used as a tool to estimate 
an approximate salary. It shouldn’t be used as an official financial 
calculator as it only considers a fixed 7.65 percent FICA tax 
(Social Security Tax – 6.20% + Medicare Tax – 1.45%) and a combined 
Tax Rate which includes Federal, State, and Local Taxes chosen by the user. 
This calculator doesn’t consider individual deductions and other 
healthcare costs as they might vary state by state 
and individual by individual.""", width=70, anchor="w", justify="left")
    disclaimerLabel.grid(row=1, column=0)
    infoLabel = Label(helpFrame1, text = """
Information about this salary calculator
                      
The purpose of Salary Calculator: Easy Pay is to allow and facilitate the process 
of generating salaries whether the user is an employer or employee.
                      
Information about the Help Window
                      
The purpose of this window is to provide instructions, 
tips, and troubleshooting assist you in using the salary calculator 
effectively.                                           
""", width=70, anchor="w", justify="left")
    infoLabel.grid(row=2, column= 0)
    howToLabel = Label(helpFrame1, text= """How to Use the Easy Pay Salary Calculator?
                       
1. First, identify yourself as an employer or an employee.
    a. If you are an employer, click on the “Employer” button.
    b. If you are an employee, click on the “Employee” button.
                       
2. Enter the required information.
    a. Overtime Pay Rate:
                       
             Explanation: A 1.5x overtime pay rate means the employee 
             earns 1.5 times their regular hourly wage for each 
             hour worked overtime.
                       
             Tip: In the U.S., the overtime rate must be at least 1.5 times
             the amount of your hourly pay rate. 1.5x is the most 
             common overtime pay rate. Refer to your company policies or 
             guidelines regarding overtime pay rates.
                       
    b. Tax Rate:
                       
             Explanation: Tax rate represents the percentage of an employee's 
             salary withheld for taxes, including federal, state, and local taxes.
                       
             Tip: This may vary state by state and individual by individual. 
             If you’re not sure visit your state website to consult your 
             local tax regulations and guidelines.
                       
3. Click the “Calculate” button to display the result.  
                       
4. To clear all entered data, click the “DELETE” button.

    Tip: Do not click unless you want to reset all textboxes in the window. 
    Clicking the “DELETE” button will allow you to enter new information 
    for calculation.             

5. To return to the main window, click the “BACK/EXIT” button.
                       
6. To access the help window, click on the “Help” button.
    a. To close the help window, click the “Close” button.
""", width=70, anchor="w", justify="left")
    howToLabel.grid(row=3, column=0)
    
    #This is the close button
    #This will close the help window
    close_button = Button(helpFrame1, text="Close", command=close_help_window)
    close_button.grid(row=4, column=0)

#This function will close the window
def close_help_window():
    global help_window_open
    global helpWindow
#destoys it
    help_window_open = False
    helpWindow.destroy()
