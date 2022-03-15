import colorgram
import turtle
from turtle import Turtle
from turtle import Screen
import random

# Define width and height of screen
WIDTH, HEIGHT = 580, 550

# Define x, y coordinates for Turtle goto()
x_coor, y_coor = 50, 50
TURTLE_SIZE = 20

# Instantiate color variable passing image and num arguments
colors = colorgram.extract('dot.jfif', 10)

# Create empty list to hold color tuples
color_list = []

# Create Screen object and setup screen
screen = Screen()
screen.setup(WIDTH,HEIGHT,0,0)

# Create turtle object 'tim' and call Turtle methods
tim = Turtle(shape="circle",visible=False)
turtle.mode("standard")
turtle.hideturtle()
turtle.colormode(255)
turtle.speed("fastest")
tim.penup()

# Create tuples from Color objects and add tuple information to color_list list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tuple_list = (r,g,b)
    color_list.append(tuple_list)

# Draw on screen a square of dots, 10 x 10, using random colors from color_list
for x in range(10):
    tim.goto((TURTLE_SIZE / 2 - screen.window_width()/ 2)+x_coor,((screen.window_height() / 2 - TURTLE_SIZE / 2) * -1) + y_coor)
    for y in range(10):
        color = random.randint(0, 9)
        tim.pencolor(color_list[color])
        tim.dot(20)
        tim.forward(50)
    y_coor+= 50

# Call goto method to move tim off the screen
tim.goto(600,600)

# Exit program on click
screen.exitonclick()