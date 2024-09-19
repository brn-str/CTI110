# Chase Burney
# 9/17/2024
# P1HW1
# Input and Output with Mathematical Expressions

print("-----Calculating Exponents-----")
print()
print()

# Get Base Value (as an integer) from the user
baseValue = int(input("Enter an integer as a base value: "))
# Get Exponent (as an integer) from the user
exponent = int(input("Enter an integer as a base value: "))
value = baseValue**exponent
print()
print (baseValue, "raised to the power of", exponent, "is", value, "!!")
print()
print()
print("-----Addition and Subtraction-----")
print()
print()
integerStart = int(input("Enter a starting integer: "))
integerAdd = int(input("Enter an integer to add: "))
integerSub = int(input("Enter an integer to subtract: "))
intSum = integerStart + integerAdd - integerSub
print()
print()
print (integerStart, "+", integerAdd, "-", integerSub, "is equal to", intSum)


