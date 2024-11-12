# Chase Burney
# 10-17-2024
# P3LAB
# Create a program to calculate the coin and paper dollar combinations from a currency input.

'''
# Regular Division
print(100/3)
print()

# Floor Division
print(100//3)
print()

# Modulus Division
print(100%3)
print()

print(7%4)
'''
userExit = "y"

while (userExit == "y"):
    # Get money value from the user
    money_U = float(input("Enter the amount of USD as a float: $"))

    # Convert money to a whole number
    money_U = int(round(money_U * 100))
    moneyCheck = money_U
    if moneyCheck < 0:
        money_U = money_U * -1
    # Calculate the amount of dollars in the money variable
    if moneyCheck >= 0:
        # Dollars
        moneyDol = money_U // 100
        if (moneyDol > 0):
            if (moneyDol == 1):
                print(f"{moneyDol} Dollar")
            else:
                print(f"{moneyDol} Dollars")

        money_U = money_U - (moneyDol* 100)

        # Quarters
        moneyQua = money_U // 25
        if (moneyQua > 0):
            if (moneyQua == 1):
                print(f"{moneyQua} Quarter")
            else:
                print(f"{moneyQua} Quarters")

        money_U = money_U - (moneyQua* 25)

        # Dimes
        moneyDim = money_U // 10
        if (moneyDim > 0):
            if (moneyDim == 1):
                print(f"{moneyDim} Dime")
            else:
                print(f"{moneyDim} Dimes")

        money_U = money_U - (moneyDim * 10)

        # Nickels
        moneyNic = money_U // 5
        if (moneyNic > 0):
            if (moneyNic == 1):
                print(f"{moneyNic} Nickel")
            else:
                print(f"{moneyNic} Nickels")

        money_U = money_U - (moneyNic * 5)

        # Pennies
        moneyPen = money_U
        if (moneyPen > 0):
            if (moneyPen == 1):
                print(f"{moneyPen} Penny")
            else:
                print(f"{moneyPen} Pennies")

        if (moneyDol == 0 and moneyQua == 0 and moneyDim == 0 and moneyNic == 0 and moneyPen == 0):
            print()
            print("No change")
    else:
        # Dollars
        moneyDol = money_U // 100
        money_U = money_U - (moneyDol* 100)
        if (moneyDol > 0):
            if (moneyDol == 1):
                moneyDol = moneyDol * -1
                print(f"{moneyDol} Dollar in Debt")
            else:
                moneyDol = moneyDol * -1
                print(f"{moneyDol} Dollars in Debt")


        # Quarters
        moneyQua = money_U // 25
        money_U = money_U - (moneyQua* 25)
        if (moneyQua > 0):
            if (moneyQua == 1):
                moneyQua = moneyQua * -1
                print(f"{moneyQua} Quarter in Debt")
            else:
                moneyQua = moneyQua * -1
                print(f"{moneyQua} Quarters in Debt")

        # Dimes
        moneyDim = money_U // 10
        money_U = money_U - (moneyDim * 10)
        if (moneyDim > 0):
            if (moneyDim == 1):
                moneyDim = moneyDim * -1
                print(f"{moneyDim} Dime in Debt")
            else:
                moneyDim = moneyDim * -1
                print(f"{moneyDim} Dimes in Debt")

        

        # Nickels
        moneyNic = money_U // 5
        money_U = money_U - (moneyNic * 5)
        if (moneyNic > 0):
            if (moneyNic == 1):
                moneyNic = moneyNic * -1
                print(f"{moneyNic} Nickel in Debt")
            else:
                moneyNic = moneyNic * -1
                print(f"{moneyNic} Nickels in Debt")

        # Pennies
        moneyPen = money_U
        if (moneyPen > 0):
            if (moneyPen == 1):
                moneyPen = moneyPen * -1
                print(f"{moneyPen} Penny in Debt")
            else:
                moneyPen = moneyPen * -1
                print(f"{moneyPen} Pennies in Debt")

        if (moneyDol == 0 and moneyQua == 0 and moneyDim == 0 and moneyNic == 0 and moneyPen == 0):
            print("No change")
    print()
    userExit = input("Do you want to restart the program? (y = yes, n = no): ")
    print()
if (userExit == "n"):
    print("The program is complete.")
if (userExit != "n" or userExit != "y"):
    print("-ERROR---ERROR---ERROR---ERROR---ERROR---ERROR---ERROR---ERROR---ERROR---ERROR-")


