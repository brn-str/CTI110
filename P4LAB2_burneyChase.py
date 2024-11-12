# Chase Burney
# 10-31-2024
# P4LAB2
# Program asks user for integer and displays multiplication

import turtle

# While loop to control program running continuously

secretChoice = 0
secretCount = 0
userType = "none"
userChoice = "none"
userValue = 0
userResult = 0
loopCheck = "y"
valid_arith = ["+", "-", "*", "/"]
while loopCheck == "y" or loopCheck == "yes":
    num1 = 1
    count = 0
    print()
    numType = input("Will your value be whole or include decimals. (W/D): ")
    if numType == "myHouse":
        print()
    else:
        numType = numType.strip()
        numType = numType.upper()
    if numType == "W" or numType == "D":
        print()
        numStand = input("Will your value be positive or negative. (+/-): ")
        numStand = numStand.strip()
        print()
        if numType == "W":
            userValue = int(input("Enter an integer: "))
        elif numType == "D":
            userValue = float(input("Enter an integer: "))
        if userValue < 0 and numStand == "+":
            print()
            print("Conflicting input.")
        elif userValue > 0 and numStand == "-":
            print()
            print("Conflicting input.")
        else:
            print()
            userChoice = input("Enter a arithmetic symbol. (+, -, *, /): ")
            print()
            print("---------------------------Output---------------------------")
            print()
            userChoice = userChoice.strip()
            if userChoice in valid_arith:
                if numType == "W":
                    if userChoice == "+":
                        for _ in range (12):
                            userResult = userValue + num1
                            print(f"{userValue} + {num1} = {userResult}")
                            num1 += 1
                    elif userChoice == "-":
                        for _ in range (12):
                            userResult = userValue - num1
                            print(f"{userValue} - {num1} = {userResult}")
                            num1 += 1
                    elif userChoice == "*":
                        for _ in range (12):
                            userResult = userValue * num1
                            print(f"{userValue} * {num1} = {userResult}")
                            num1 += 1
                    elif userChoice == "/":
                        for _ in range (12):
                            userResult = userValue / num1
                            print(f"{userValue} / {num1} = {round(userResult)}")
                            num1 += 1
                    else:
                        print ("Invalid arithmetic")
                elif numType == "D":
                    if userChoice == "+":
                        for _ in range (12):
                            userResult = userValue + num1
                            print(f"{userValue} + {num1} = {userResult:.2f}")
                            num1 += 1
                    elif userChoice == "-":
                        for _ in range (12):
                            userResult = userValue - num1
                            print(f"{userValue} - {num1} = {userResult:.2f}")
                            num1 += 1
                    elif userChoice == "*":
                        for _ in range (12):
                            userResult = userValue * num1
                            print(f"{userValue} * {num1} = {userResult:.2f}")
                            num1 += 1
                    elif userChoice == "/":
                        for _ in range (12):
                            userResult = userValue / num1
                            print(f"{userValue} / {num1} = {userResult:.2f}")
                            num1 += 1
            else:
                print()
                print ("Invalid arithmetic")
    elif numType == "myHouse":
        window = turtle.Screen()
        tom = turtle.Turtle()
        tom.pensize(8)
        tom.pencolor("red")
        tom.shape("circle")
        
        count1 = 0
        while count1 <= 3:
            count1 += 1
            tom.forward(125)
            tom.right(90)
        
        tom.right(180)
            
        count1 = 0
        while count1 <= 3:
            count1 += 1
            tom.forward(125)
            tom.right(90)
            
        count1 = 0
        while count1 <= 3:
            count1 += 1
            tom.forward(125)
            tom.left(90)
        
        tom.right(180)
            
        count1 = 0
        while count1 <= 3:
            count1 += 1
            tom.forward(125)
            tom.left(90)

        tom.forward(125)
        tom.left(90)
        tom.forward(125)
        tom.left(45)

        count1 = 0
        while count1 <= 1:
            count1 += 1
            tom.forward(175)
            tom.left(90)
                
    print()
    print("------------------------------------------------------------")
    print()
    if secretCount <= 5:
        secretChoice += 1
        secretCount += 1
    if secretChoice == 5:
        print("type 'myHouse' into the 'whole or decimal' prompt for a secret.")
        print()
        secretChoice = 0
    loopCheck = input("Run program again? ")
    loopCheck = loopCheck.lower()
    loopCheck = loopCheck.strip()
    if loopCheck == "y" or loopCheck == "yes":
            print()
            print("------------------------------------------------------------")

# The loop breaks
print("Program terminated.")







































