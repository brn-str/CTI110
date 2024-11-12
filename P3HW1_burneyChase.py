# Chase Burney
# 10-10-24
# P2HW2
# Create a code to use 6 grades and find the lowest grade, highest grade, sum of grades, and the average of the grades

print()
print("<------------MODULE GRADE CALCULATOR------------>")
print()
# Save the users input into variabvle for later use
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Compile the variables with input given by the user into a list
modList = [mod1, mod2, mod3, mod4, mod5, mod6]

# Find the minimum and maximum values of the Module list
modMin = min(modList)
modMax = max(modList)

# Find the sum and length of the Module list
modSum = sum(modList)
modLen = len(modList)

# Divide the sum by the length to find the average of the Module list
modAvg = modSum / modLen
print()
print("<--------------------RESULTS-------------------->")
print()

# Display the minimum, maximum, sum, and average to the user
print(f"{'Lowest Grade:':<20} {modMin:,.2f}")
print(f"{'Highest Grade:':<20} {modMax:,.2f}")
print(f"{'Sum of Grades:':<20} {modSum:,.2f}")
print(f"{'Average:':<20} {modAvg:,.2f}")

# Branching to determine the letter grade

print()
print("<---------------------GRADE--------------------->")
print()
letter_grade = "placeholder"
if modAvg <=100 and modAvg >= 90:
    letter_grade = "A"
elif modAvg <=89 and modAvg >= 80:
    letter_grade = "B"
elif modAvg <=79 and modAvg >= 70:
    letter_grade = "C"
elif modAvg <=69 and modAvg >= 60:
    letter_grade = "D"
elif modAvg <60:
    letter_grade = "F"
else:
    letter_grade = "INVALID AVERAGE"
    print("                 INVALID AVERAGE                 ")
    print("                 RESTART PROGRAM                 ")

if letter_grade != "INVALID AVERAGE":
    print(f"Your grade is {letter_grade}")

print()
print("<----------------------END---------------------->")

'''
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
modList = (mod1, mod2, mod3, mod4, mod5, mod6)
modMin = min(modList)
modMax = max(modList)
modSum = sum(modList)
modLen = len(modList)
modAvg = modSum / modLen
display("Lowest Grade:", modMin)
display("Highest Grade:", modMax)
display("Sum of Grades:", modSum)
display("Average:", modAvg")
'''
