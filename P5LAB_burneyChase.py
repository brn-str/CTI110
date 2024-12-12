# Chase Burney
# 11-14-2024
# P5LAB
# Use functions to simulate a self checkout

import random

# Define the main
def main():
    debugStore = 'y'
    print()
    while(debugStore == 'y'):
        print("******Welcome to self-checkout!!!******")
        print()
        leftOver = calcCashback()
        disperseCashback(leftOver)
        print()
        print("***************************************")
        print()
        result = input("Continue testing system? (y/n): ")
        debugStore = result.lower()
        print()
        print("***************************************")
        print()

def calcCashback():

    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    userCash = float(input("How much cash will you put in the self-checkout? "))

    userChange = userCash - total_owed

    return userChange

def disperseCashback(leftOver):

    print(f"Change is: ${leftOver:.2f}")
    print()
    
    money_U = leftOver
     
    # Convert money to a whole number
     
    money_U = int(round(money_U * 100))
     
    moneyCheck = money_U

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
         
            print("No change due.")
     
   

# Call the main
if __name__ == "__main__":
    main()
