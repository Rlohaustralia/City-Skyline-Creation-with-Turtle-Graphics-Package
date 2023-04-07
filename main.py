# City Skyline Creation with Turtle Graphics Package

import turtle
import random


def setBackground():
    turtle.setup(540, 540)
    turtle.bgcolor('light blue')

    turtle.fillcolor('black')
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(-240, 240)
    turtle.goto(240, 240)
    turtle.goto(240, -240)
    turtle.goto(-240, -240)
    turtle.goto(-240, 240)
    turtle.pendown()
    turtle.end_fill()


def drawStar():
    turtle.fillcolor('white')

    for star in range(10):
        star_range_x = random.uniform(-230, 230)
        star_range_y = random.uniform(40, 230)
        turtle.penup()
        turtle.goto(star_range_x, star_range_y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()


def drawOutline():
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.penup()

    turtle.goto(-240, -40)
    turtle.goto(240, -40)
    turtle.goto(240, -240)
    turtle.goto(-240, -240)
    turtle.goto(-240, -40)

    turtle.goto(-180, -40)
    turtle.goto(-180, 60)
    turtle.goto(-120, 60)
    turtle.goto(-120, 180)
    turtle.goto(0, 180)
    turtle.goto(0, 0)
    turtle.goto(60, 0)
    turtle.goto(60, 120)
    turtle.goto(140, 120)
    turtle.goto(140, 40)
    turtle.goto(180, 40)
    turtle.goto(180, -40)

    turtle.goto(240, -40)
    turtle.goto(-240, -40)

    turtle.pendown()
    turtle.end_fill()


def drawWindow():

    turtle.fillcolor('white')

    starting_point_x = [-160, -100, -100, -40, -20, 80]
    starting_point_y = [40, 160, 140, -40, 120, 100]
    for i in range(len(starting_point_x)):
        x = starting_point_x[i]
        y = starting_point_y[i]

        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x, y)
        turtle.goto(x + 10, y)
        turtle.goto(x + 10, y - 10)
        turtle.goto(x, y - 10)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.end_fill()

        i += 1


def main():
    turtle.hideturtle()
    turtle.speed(10)
    setBackground()
    drawStar()
    drawOutline()
    drawWindow()
    turtle.done()

main()