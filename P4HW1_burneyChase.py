# Chase Burney
# 11-05-2024
# P4HW1
# Valid input of scores taken and lowest score dropped before find an average

# Value to tell how many times to iterate loop
numGrade = int(input("Enter the number of grades you wish to enter: "))

# List to hold valid inputs later
validGrade = []

txt1 = "Enter score #"
txt2 = ": "
txt2Alt = " again: "

for item in range(numGrade):
    userInput = float(input(f"{txt1:>15}{item + 1}{txt2}"))
    while userInput > 100 or userInput < 0:
        print("Invalid score, please enter a value between 0 and 100.")
        userInput = float(input(f"{txt1:>15}{item + 1}{txt2Alt}"))
    validGrade.append(userInput)

lowTxt = "Lowest Score"
modTxt = "Modified List"
avgTxt = "Scores Average"
grdTxt = "Grade"
dotDot = ":"
emptySpace = " "
grade = "N"
validSum = 0
validAvg = 0

print()
print("---------------Results---------------")
print(f"{lowTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{min(validGrade)}")
validGrade.remove(min(validGrade))
print(f"{modTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{validGrade}")
validSum = sum(validGrade)
numGrade = numGrade - 1
validAvg = validSum / numGrade
print(f"{avgTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{validAvg}")
if validAvg <= 100 and validAvg >= 90:
    grade = "A"
    print(f"{avgTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{grade}")
elif validAvg <= 89 and validAvg >= 80:
    grade = "B"
    print(f"{avgTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{grade}")
elif validAvg <= 79 and validAvg >= 70:
    grade = "C"
    print(f"{avgTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{grade}")
elif validAvg <= 69 and validAvg >= 60:
    grade = "D"
    print(f"{avgTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{grade}")
else:
    grade = "F"
    print(f"{avgTxt}{emptySpace:>5}{dotDot}{emptySpace:>5}{grade}")
