# Chase Burney
# 10-24-24
# P3HW2
# Calculate regular and over time pay given an employee's hours worked.

'''
# --- Declare variables ---
# Declare String userName
# Declare int totalHour, workHour
# Declare float payRate, overHour, overPay, regPay, grossPay

# --- Get user input ---
# userName = input "Enter employee name: "
# totalHour = input "Enter number of hours worked: "
# payRate = input "Enter employee's pay rate: "

# --- Calculations ---
# if totalHour > 40
#   overHour = totalHour - 40
# else
#   overHour = 0
#
# workHour = totalHour - overHour
#
# if overHour != 0
#   overPay = overHour * payRate * 1.5
# else
#   overPay = 0
#
# regPay = workHour * payRate
#
# grossPay = regPay + overPay
# 
#
# --- Output ---
# Display total hours worked
# Display regular pay rate
# Display overtime hours worked
# Display overtime payj
# Display regular pay
# Display total pay (reg + overtime pay)
'''

userName = input ("Enter employee name: ")
totalHour = float(input ("Enter number of hours worked: "))
payRate = float(input ("Enter employee's pay rate: "))
print("-------------------------------------------------------------------------------------------------------------")
if (totalHour > 40):
    overHour = totalHour - 40
else:
    overHour = 0

workHour = totalHour - overHour

if (overHour != 0):
    overPay = overHour * payRate * 1.5
else:
    overPay = 0

regPay = workHour * payRate

grossPay = regPay + overPay

print(f"Employee name: {userName}")
print()
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-------------------------------------------------------------------------------------------------------------")
print(f"{totalHour:<20}{payRate:<20}{overHour:<20}{overPay:<20}{regPay:<20}{grossPay:<20}")
