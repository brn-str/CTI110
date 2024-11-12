# Chase Burney
# 10/01/2024
# P2LAB1
# Using built-in libraries for circle calculations

# Import the math library
import math

# Create a variable to hold pi
pi = math.pi

print(f"{pi}")
print()

# Get radius from user
radius = float(input('What is the radius of the circle? '))
print()

# Calculate and display the diameter
diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}")
print()

circumf = 2 * pi * radius
circumf_R = round(circumf) 
print(f"The circumference of the circle is {circumf:.2f}")
print()
print(f"The rounded circumference of the circle is {circumf_R}")
print()

area = math.pi * radius**2
print(f"The area of the circle is {area:.3f}")
print()
