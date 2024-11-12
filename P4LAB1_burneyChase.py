# Chase Burney
# 10/29/2024
# P4LAB1
# Use loops and turtle library to draw a house

# Import turtle library
import turtle

# Set window and
window = turtle.Screen()
tom = turtle.Turtle()

# Changes features of turtle
tom.pensize(10)
tom.pencolor("purple")
tom.shape("arrow")

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


