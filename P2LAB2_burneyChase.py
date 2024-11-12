# Chase Burney
# 10 - 03 - 24
# P2LAB2
# create a program to allow asuer to input their vehicle and how mny gallons needeed to drive

# car_data = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
car_data = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
# A "user translation" key has been added to aloow the .lower() version of the key to show the properly capitalized key name
user_trans = {"camaro":"Camaro", "prius":"Prius", "model s":"Model S", "silverado":"Silverado"}
keys = car_data.keys()
'''
car_data["camaro"] = 18.21
car_data["prius"] = 52.36
car_data["model s"] = 110
car_data["silverado"] = 26
'''
# Print the dictionary keys
print(keys)
print()
# Get input from the user about which car to use
user_car_input = input("Enter a vehicle name to see it's mpg: ")
# Translate the use input into the original dictionary's key terms
car_trans = user_car_input.lower()
user_car = user_trans[car_trans]
print()
# Find the value from the user's input
user_car_data = car_data[user_car]
# Print the chosen user car and how much mpg it gets
print(f"The {user_car} gets {user_car_data} mpg.")
print()
# Prompt the user to input the miles they will drive
user_miles = float(input(f"How many miles will you drive the {user_car}? "))
# Calculate the gallons needed using both of the user's input
user_gas = user_miles / user_car_data 
print()
# Print the gallon(s) needed to drive the amount of miles specified by the user in the car also specified by the user
print(f"{user_gas:.2f} gallon(s) of gas are needed to drive the {user_car} {user_miles} miles.")
