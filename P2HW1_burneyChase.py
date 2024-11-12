#Chase Burney
#09/26/24
#P2HW1
#Reformatting P1HW2

#Budgeting travel for a user by using their input.

print("<--------------------------------------------------->")
print("<---------------JojaTravel Calculator--------------->")
print("<--------------------------------------------------->")
print()
#Get user input about travel desination and expenses
name = input ("Enter your name: ")
budget = float(input("Enter your budget: $"))
destination = input("Enter your destination of travel: ")
fuel = float(input("Enter projected fuel costs: $"))
acom = float(input("Enter projected acommodation costs: $"))
food = float(input("Enter projected food costs: $"))
#Calculate the remainder for the budget
remainder = budget - (fuel + acom + food)
print()
print("<--------------------------------------------------->")
print("<------------------Travel Expenses------------------>")
print("<--------------------------------------------------->")
print()
print(f"{'Travel Destination:':<25} {destination:}")
print(f"{'Initial Budget:':<25} ${budget:,.2f}")
print()
print(f"{'Fuel:':<25} ${fuel:,.2f}")
print(f"{'Acommodation:':<25} ${acom:,.2f}")
print(f"{'Food:':<25} ${food:,.2f}")
print()
print("-----------------------------------------------------")
print()
print(f"Remaining Budget: ${remainder:,.2f}")
print()
if (remainder > 0):
    print(f"Good luck in {destination}, {name}!")
else:
    print(f"{destination} is outside of your budget {name}.")
print()
print("<--------------------------------------------------->")
print("<-----------------Have A Great Day!----------------->")
print("<--------------------------------------------------->")
print("< H       H       H       H       H       H       H >")
print("<     A       A       A       A       A       A     >")
print("< V       V       V       V       V       V       V >")
print("<     E       E       E       E       E       E     >")
print("< A       A       A       A       A       A       A >")
print("<     G       G       G       G       G       G     >")
print("< R       R       R       R       R       R       R >")
print("<     E       E       E       E       E       E     >")
print("< A       A       A       A       A       A       A >")
print("<     T       T       T       T       T       T     >")
print("< D       D       D       D       D       D       D >")
print("<     A       A       A       A       A       A     >")
print("< Y       Y       Y       Y       Y       Y       Y >")
print("<--------------------------------------------------->")
print("<------------------JojaCorporation------------------>")
print("<--------------------------------------------------->")

# Practice Formatting:
'''
# Width formatting using the f-string
print("\n\n")
print("C.R.E.A.M")
print("<><>" * 20)
expense_name = "EXPENSE NAME"

# Print the heading row
print(f"{expense_name:<18}{'MONTHLY COST':<15}{'ANNUAL COST'}")

# Print the rest of the rows
month_phone = 107.88888
annual_phone = month_phone * 12
'''
