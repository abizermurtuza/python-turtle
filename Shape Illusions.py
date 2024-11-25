import turtle
from math import sqrt


# Group: Hans, Abizer & Yingwei
# Date: October 5, 2023
# Assignment 1: Introduction to Turtle Programming
# Project Name: Shape Illusions


# Variables
screen = turtle.Screen()  # Screen
t = turtle.Turtle()  # Turtle
scale = 50  # Scale variable for consistent scaling
angle = 0  # Angle for setting the angle in a repeating shape
direction = "Right"  # Direction for Blue Cube side
changeCoordinate = 0  # Used for setting the coordinates depending on the value
x = 0  # x coordinates
y = 0  # y coordinates


# Appearance/ General
screen.bgcolor("black")  # Sets Background color
screen.title("SHAPE ILLUSIONS")  # Sets Screen name
turtle.setworldcoordinates(-500, -500, 500, 500)  # Sets a user defined coordinates system for scaling
t.color("black")  # Sets Turtle Color
t.speed(150)  # Sets speed




# Creates a function to set the coordinates for the shapes and message
def coordinates(x, y):
   if changeCoordinate == 1:  # Checks the value of changeCoordinates and gives a new set of values for x and y
       x, y = -100, -50
   elif changeCoordinate == 2:
       x, y = 250, 150
   elif changeCoordinate == 3:
       x, y = 250, -250
   elif changeCoordinate == 4:
       x, y = -250, 250
   elif changeCoordinate == 5:
       x, y = -250, -250
   elif changeCoordinate == 6:
       x, y = -400, -50  # Coordinates for the messages
   elif changeCoordinate == 7:
       x, y = -397, -47
   else:
       x, y = -394, -44
   return x, y  # Returns the values for x and y coordinates




# Primary Contributor: Yingwei for Middle Shape
# Secondary Contributors: Hans & Abizer for touch-ups and fixing
# Upper pink section
t.penup()
changeCoordinate += 1  # Adds 1 to changeCoordinate for the first shape
t.goto(coordinates(x, y))  # Sets the coordinates for the turtle to start creating the shape
t.fillcolor('#FF1CB4')  # Hex Value of the pink color, found using a hex color picker online
t.begin_fill()  # Starts filling color
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(45)
t.forward(30)
t.right(45)
t.backward(190)
t.left(90)
t.forward(55)
t.right(90)
t.forward(150)
t.left(45)
t.forward(33)
t.right(45)
t.backward(205)
t.end_fill()  # Ends filling color


# Lower light blue section
t.fillcolor('#00E1F1')  # Hex Value of the light blue color wanted
t.begin_fill()
t.right(135)
t.backward(33)
t.right(45)
t.backward(199)
t.right(90)
t.backward(102)
t.right(90)
t.backward(190)
t.right(135)
t.backward(30)
t.right(45)
t.backward(145)
t.right(90)
t.forward(58)
t.right(90)
t.backward(195)
t.right(180)
t.backward(195)
t.end_fill()


# Left corner dark blue section
t.fillcolor('#252DC0')  # Hex Value of the dark blue color wanted
t.begin_fill()
t.right(135)
t.backward(34)
t.left(225)
t.forward(34)
t.left(90)
t.forward(24)
t.right(90)
t.backward(53)
t.left(135)
t.end_fill()  # Ends shape coloring here
t.backward(33)  # Left to right transition
t.left(45)
t.backward(30)
t.right(90)
t.backward(120)


# Right corner dark blue section
t.fillcolor('#252DC0')  # Hex Value of the dark blue color wanted
t.begin_fill()
t.left(45)
t.backward(32)
t.right(135)
t.backward(55)
t.right(90)
t.backward(23)
t.right(90)
t.backward(32)
t.end_fill()
t.penup()


# Primary Contributor: Abizer & Hans for Blue Shape
# Top Light Blue Section
changeCoordinate += 1  # Adds 1 to changeCoordinate for the second shape
t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
t.setheading(90)
t.forward(2.5 * scale)
t.fillcolor("#00F8FF")  # Hex Value of light blue
t.begin_fill()
t.setheading(25)
t.forward(3.5 * scale)
t.left(130)
t.forward(3.5*scale)
t.left(50)
t.forward(3.5 * scale)
t.left(130)
t.forward(3.5 * scale)
t.right(65)
t.end_fill()


# Top Black Section, to cover the previous light blue covering everything
t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
t.setheading(90)
t.forward(3.25 * scale)
t.fillcolor("Black")  # No need for hex of Black
t.begin_fill()
t.right(65)
t.forward(2 * scale)
t.left(130)
t.forward(2 * scale)
t.left(50)
t.forward(2 * scale)
t.left(130)
t.forward(2 * scale)
t.right(65)
t.forward(1 * scale)
t.end_fill()


# Left and Right sections of the shape
for i in [1, 2]:  # Repeats twice for both left side and right side
   t.penup()  # Geneal positioning for both sides
   t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
   t.setheading(90)
   t.backward(0.5 * scale)
   t.forward(0.5*scale)
   if direction == "Right":  # Right Side
       # Right Side Large Section
       t.fillcolor("#076DAB")  # Hex Value of a Blue color
       t.begin_fill()
       t.forward(2.5*scale)
       t.right(65)
       t.forward(3.5*scale)
       t.right(115)
       t.forward(4*scale)
       t.right(65)
       t.forward(3.5*scale)
       t.right(115)
       t.forward(0.5*scale)
       t.right(65)
       t.forward(3*scale)
       t.left(65)
       t.forward(3*scale)
       t.left(115)
       t.forward(2.25*scale)
       t.left(65)
       t.forward(2*scale)
       t.right(65)
       t.forward(0.75*scale)
       t.end_fill()
       t.penup()


       # Right Side Inner Section
       t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
       t.setheading(90)
       t.forward(2 * scale)
       t.right(65)
       t.forward(2 * scale)
       t.fillcolor("#00ABCE")  # Hex Value of a Blue color
       t.begin_fill()
       t.forward(1 * scale)
       t.right(115)
       t.forward(3 * scale)
       t.right(115)
       t.forward(1 * scale)
       t.right(65)
       t.forward(2 * scale)
       t.end_fill()
       t.penup()


       # Top Right Side Inner Section
       t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
       t.setheading(90)
       t.forward(3.25 * scale)
       t.right(65)
       t.forward(1.5 * scale)
       t.fillcolor("#05A6D4")  # Hex Value of a Blue color
       t.begin_fill()
       t.left(130)
       t.forward(1.5 * scale)
       t.right(65)
       t.forward(0.45 * scale)
       t.right(115)
       t.forward(2.05 * scale)
       t.right(130)
       t.forward(0.5 * scale)
       t.end_fill()
       t.penup()
   else:  # Left Side
       # Left Side Large Section
       t.fillcolor("#01A7D7")  # Hex Value of a Blue color
       t.begin_fill()
       t.forward(2.5 * scale)
       t.left(65)
       t.forward(3.5 * scale)
       t.left(115)
       t.forward(4 * scale)
       t.left(65)
       t.forward(3.5 * scale)
       t.left(115)
       t.forward(0.5 * scale)
       t.left(65)
       t.forward(3 * scale)
       t.right(65)
       t.forward(3 * scale)
       t.right(115)
       t.forward(2.25 * scale)
       t.right(65)
       t.forward(2 * scale)
       t.left(65)
       t.forward(0.75 * scale)
       t.end_fill()
       t.penup()


       # Left Side Inner Section
       t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
       t.setheading(90)
       t.forward(2 * scale)
       t.left(65)
       t.forward(2 * scale)
       t.fillcolor("#066DB2")  # Hex Value of a Blue color
       t.begin_fill()
       t.forward(1 * scale)
       t.left(115)
       t.forward(3 * scale)
       t.left(115)
       t.forward(1 * scale)
       t.left(65)
       t.forward(2 * scale)
       t.end_fill()
       t.penup()


       # Top Left Side Inner Section
       t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
       t.setheading(90)
       t.forward(3.25 * scale)
       t.left(65)
       t.forward(1.5 * scale)
       t.fillcolor("#0C71A9")  # Hex Value of a Blue color
       t.begin_fill()
       t.right(130)
       t.forward(1.5 * scale)
       t.left(65)
       t.forward(0.45 * scale)
       t.left(115)
       t.forward(2.05 * scale)
       t.left(130)
       t.forward(0.5 * scale)
       t.end_fill()
       t.penup()
   direction = "left"  # Changes the Direction to left after finishing the right side then repeats the whole loop


# Creates the Bottom light blue shape
t.goto(coordinates(x, y))  # Sets the coordinates for the second shape
t.setheading(25)
t.fillcolor("#00E5FF")  # Hex Value of a Light Blue color
t.begin_fill()
t.forward(2 * scale)
t.right(57.5)
t.forward(1.05 * scale)
t.right(122.5)
t.forward(3 * scale)
t.right(50)
t.forward(3 * scale)
t.right(122.5)
t.forward(1.05 * scale)
t.right(57.5)
t.forward(2 * scale)
t.end_fill()
t.penup()


# Primary Contributor: Hans for Pink Shape
changeCoordinate += 1   # Adds 1 to changeCoordinate for the third shape
for color in ["#E051CF", "#80186D", "#AC339A", "#DA54CF", "#F56FEC"]:  # Loops for the hex colors of pink
   t.goto(coordinates(x, y))  # Sets the positioning for the third shape
   t.setheading(angle)  # Starts at angle 0
   t.forward(3*scale/sqrt(5))  # Goes forward to position current shape to be beside the next shape
   t.left(125)  # This square roots 5 since the shape repeats 5 times and is a pentagon
   t.forward(1.5*scale)
   t.begin_fill()  # Starts coloring
   t.fillcolor(color)  # Sets the color for the loop
   t.forward(1*scale)  # Creates the shape
   t.left(72)
   t.forward(3*scale)
   t.left(72)
   t.forward(2.75*scale)
   t.left(50)
   t.forward(1.3*scale)
   t.left(130)
   t.forward(3*scale)
   t.right(72)
   t.forward(2.5*scale)
   t.end_fill()  # Ends coloring
   angle = angle + 72  # Sets the angle for the next shape, 72 since 360/5 = 72
   t.penup()


# Primary Contributor: Hans for Green Shape
changeCoordinate += 1   # Adds 1 to changeCoordinate for the fourth shape
for color in ["#016738", "#00B558", "#017D3E", "#38BC4C"]:  # Loops for the hex colors of green
   t.goto(coordinates(x, y))  # Same process as the Pink Pentagon
   t.setheading(angle)
   t.forward(3.25*scale/sqrt(4))  # Square roots 4 since there are four shapes
   t.right(135)
   t.begin_fill()
   t.fillcolor(color)
   t.forward(3*scale)
   t.right(90)
   t.forward(3.75*scale)
   t.left(135)
   t.forward(1*scale)
   t.left(45)
   t.forward(3.75*scale)
   t.left(90)
   t.forward(3.75*scale)
   t.end_fill()
   angle = angle + 90  # Sets next angle for next shape, 90 since 360/4 = 90
   t.penup()


# Primary Contributor: Hans for Red Shape
changeCoordinate += 1   # Adds 1 to changeCoordinate for the fifth shape
for color in ["#C8121E", "#E71E28", "#FF4C36"]:  # Loops for the hex colors of red
   t.goto(coordinates(x, y))  # Same process as previous two
   t.setheading(angle)
   t.forward(2*scale/sqrt(3))  # Square roots 3 since there are three shapes
   t.left(150)
   t.begin_fill()
   t.fillcolor(color)
   t.forward(3*scale)
   t.left(120)
   t.forward(5*scale)
   t.left(120)
   t.forward(6*scale)
   t.left(60)
   t.forward(1*scale)
   t.left(120)
   t.forward(5*scale)
   t.right(120)
   t.forward(3*scale)
   t.end_fill()
   angle = angle + 120  # Sets next angle for next shape, 120 since 360/3 = 120
   t.penup()


# Primary Contributor: Hans for the Message
# Writes the text "SHAPE ILLUSIONS" at the middle of the screen in multiple colors
for color in ["Black", "Pink", "Red"]:  # Loops for every color
   changeCoordinate += 1  # Adds 1 to changeCoordinate for the message location in each loop
   t.goto(coordinates(x, y))  # Sets position
   t.color(color)  # Changes color
   t.write("SHAPE ILLUSIONS", font=("Labrat", 64, "bold"))  # Creates text with a font, a size and bolded
t.color("Black")  # Makes the turtle invisible for the end of the program


# Keeps window open until a click
screen.exitonclick()