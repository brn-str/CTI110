# Chase Burney
# 11-05-2024
# P4HW2
# Make a program to calculate the gross pay for multiple employees

empName = ""
lowerName = ""
totalHour = 0
overHour = 0
workHour = 0
payRate = 0
overPay = 0
regPay = 0
grossPay = 0
emptySpace = " "
nameInc = 0
overInc = 0
regInc = 0
grossInc = 0
empList = []
grossList = []
forCount = 0
intro = 0
colon = ":"

print()
empName = input("Enter employee's name or " + '"done"' + " to terminate: ")
lowerName = empName.lower()
if empName != "done":
    nameInc = 1
    empList.append(empName)
while not lowerName == "done":
    totalHour = float(input("How many hours did " + empName + " work? "))
    payRate = float(input("What is " + empName + "'s pay rate? "))
    print("")
    print(f"Employee name:{emptySpace:>3}{empName}")
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

    grossList.append(grossPay)
    
    overInc = overInc + overPay
    regInc = regInc + regPay
    grossInc = grossInc + grossPay

    print()
    print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("-------------------------------------------------------------------------------------------------------------")
    print(f"{totalHour:<20}{payRate:<20}{overHour:<20}{overPay:<20}{regPay:<20}{grossPay:<20}")
    print("")
    print("")
    empName = input("Enter employee's name or " + '"Done"' + " to terminate: ")
    lowerName = empName.lower()
    if empName != "done":
        nameInc = nameInc + 1
        empList.append(empName)

if nameInc != 0: 
    print("")
    print(f"Total number of employeees entered: {nameInc}")
    print(f"Total amount paid for overtime hours: ${overInc}")
    print(f"Total amount paid for regular hours ${regInc}")
    print(f"Total amount paid in gross: ${grossInc}")
    print("")
    detail = input("Do you wish to see more info? (y/n): ")
    print("")
    if detail == 'y':
        for item in range(nameInc):
            if intro < 1:
                print(f"Employee Name{emptySpace:>1}{colon:>2}{emptySpace:>2}Gross Pay")
                print("---------------------------")
            print(f"{empList[forCount]}{emptySpace:>1}{colon:>2}{emptySpace:>2}{grossList[forCount]}")
            forCount = forCount + 1
            intro = intro + 1
else:
    print()
    print("THE PROGRAM HAS BEEN TERMINATED.")
            













    
