"""
The purpose of this module is to provide functions for calculating and displaying 
salary-related information for both employers and employees.
It includes functions to calculate gross and net pay, tax deductions, 
and other relevant financial details based on the input provided.
"""
#--------------------For the Employer Window------------------
#This function will calculate and display the salary information for an employee.
# It takes input parameters yourName, employeeName, workedHours, hourlySalary,
# overtimeRate, and taxRate.


def calculateAndDisplaySalary(yourName, employeeName, workedHours, hourlySalary, overtimeRate, taxRate):
     #This will convert overtime rate and tax rate from percentage to decimal
    taxRate /= 100

    #This will calculate gross pay based on hours worked and hourly salary
    grossPay = workedHours * hourlySalary

    #I initialized overtime pay to zero because it will allow me to
    #Display it, even if there is no overtime
    overtimePay =0.0
    normalPay = grossPay #This will allow me to meet at the return requirements
    taxReduction = grossPay * taxRate

    #This will calculate FICA taxes
    #This tax is related to social security and medicare
    #It takes 7.65% of a paycheck
    ficaTaxes = grossPay* 0.0765
    netPay = grossPay - taxReduction - ficaTaxes #netpay is after taxes and deductions
    #This will check if the worked hours exceeds 40 hrs
    #It will calculate overtime pay and taxes
    if workedHours > 40:
        overtimeHours = workedHours - 40
        overtimePay = hourlySalary * overtimeRate * overtimeHours
        normalPay = 40 * hourlySalary
        grossPay = normalPay + overtimePay
        taxReduction = grossPay * taxRate
        ficaTaxes = grossPay * 0.0765
        netPay = float((grossPay - taxReduction) - ficaTaxes)

    #This will be all the information displayed to the user  
    result_text = f"Hello, {yourName}. Here is the information:\n"
    result_text += f"Hours Worked by {employeeName}: {workedHours}\n"
    result_text += f"Hourly Salary: ${hourlySalary}\n"
    result_text += f"Overtime Pay Rate: {overtimeRate}\n" 
    result_text += f"Gains from regular hours: ${normalPay}\n"
    result_text += f"Gains from overtime hours: ${overtimePay}\n" #This one will display 0.0 if there's no overtime
    result_text += f"Tax Deductions (Tax Rate): ${taxReduction}\n"
    result_text += f"FICA Tax (7.65%): ${ficaTaxes}\n"
    result_text += f"Gross Salary (Before Taxes): ${grossPay}\n"
    result_text += f"Net Pay (After Taxes): ${netPay}"

     #returns/display the results   
    return result_text 
"""
My variables:
yourName - The name of the user using the application (Employer).
employeeName - The name of the employee.
workedHours -The number of hours worked by the employee.
hourlySalary -The hourly salary rate of the employee.
overtimeRate- The overtime pay rate multiplier.
taxRate- The tax rate as a percentage. 
"""

#--------------------For the Employee Window------------------
#Almost the same at the one for the employer window.
#This helped me solve one bug caused by the difference in 
#the amount of arguments in each window
#It will check if there are more than 40 hours worked, calculate taxes,
#and display the result.

def calculateAndDisplayEmployeeSalary(user_name, worked_hours, hourly_salary, overtime_rate, tax_rate):
    #This will convert tax rate from percentage to decimal
    tax_rate /= 100

    #calculates the net and gross if the worked hours are less than 40
    gross_pay = worked_hours * hourly_salary
    overtime_pay = 0.0
    normal_pay = gross_pay
    tax_reduction = gross_pay * tax_rate
    fica_taxes = gross_pay * 0.0765
    net_pay = gross_pay - tax_reduction - fica_taxes

     #calculates the net and gross if the worked hours are more than 40  
    if worked_hours > 40:
        overtime_hours = worked_hours - 40
        overtime_pay = hourly_salary * overtime_rate * overtime_hours
        normal_pay = 40 * hourly_salary
        gross_pay = normal_pay + overtime_pay
        tax_reduction = gross_pay * tax_rate
        fica_taxes = gross_pay * 0.0765
        net_pay = float((gross_pay - tax_reduction) - fica_taxes)

    #all the info that is going to be displayed
    result_text = f"Hello, {user_name}. Here is the information:\n"
    result_text += f"Hours Worked: {worked_hours}\n"
    result_text += f"Hourly Salary: ${hourly_salary}\n"
    result_text += f"Overtime Pay Rate: {overtime_rate}\n"
    result_text += f"Gains from regular hours: ${normal_pay}\n"
    result_text += f"Gains from overtime hours: ${overtime_pay}\n"
    result_text += f"Tax Deductions (Tax Rate): ${tax_reduction}\n"
    result_text += f"FICA Tax (7.65%): ${fica_taxes}\n"
    result_text += f"Gross Salary (Before Taxes): ${gross_pay}\n"
    result_text += f"Net Pay (After Taxes): ${net_pay}"
        
    #returns/display the results   
    return result_text
"""
My variables:
user_name - The name of the user (Employee).
worked_hours- The number of hours worked by the employee.
hourly_salary- The hourly salary rate of the employee.
overtime_rate - The overtime pay rate multiplier.
tax_rate- The tax rate as a percentage.
"""