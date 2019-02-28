import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()

wn = turtle.Screen()
t1.screen.reset()
t1.screen.setworldcoordinates(0, 0, 500, 500)
t2.screen.reset()
t2.screen.setworldcoordinates(0, 0, 500, 500)


def star(t, size):
    t.left(72)
    t.color('white')
    t.fillcolor('white')
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

wn.bgcolor('black')
star_pencil = turtle.Turtle()
star_pencil.color('white')
star_pencil.penup()
star_pencil.speed(0)

for i in range(20):
    star_pencil.setposition(random.randrange(0, 500), random.randrange(200, 500))
    star(star_pencil, random.randrange(1, 6))
star_pencil.hideturtle()



t2.speed(0)
t2.pencolor('dark slate gray')
t2.pensize(5)
t2.fillcolor('dark slate gray')
t2.begin_fill()
t2.goto(0,350)
t2.right(20)
for i in range(5):
    for i in range(6):
        t2.forward(random.randrange(10, 20))
        t2.right(90)
        t2.forward(random.randrange(10))
        t2.left(90)
    t2.forward(random.randrange(10, 20))
    t2.right(90)
    t2.forward(random.randrange(10))
    t2.left(90)
t2.goto(500, 0)
t2.home()
t2.hideturtle()
t2.end_fill()

t1.speed(0)
t1.pencolor('midnight blue')
t1.pensize(5)
t1.fillcolor('midnight blue')
t1.begin_fill()
t1.left(45)
for i in range(6):
    for i in range(6):
        t1.forward(random.randrange(10, 20))
        t1.right(90)
        t1.forward(random.randrange(10))
        t1.left(90)
    t1.forward(random.randrange(10, 20))
    t1.right(90)
    t1.forward(random.randrange(10))
    t1.left(90)
t1.goto(t1.xcor(), 0)
t1.home()
t1.hideturtle()
t1.end_fill()

moon_pencil = turtle.Turtle()
moon_pencil.color('slate gray')
moon_pencil.speed(0)
moon_pencil.penup()
moon_pencil.setposition(25, 400)
moon_pencil.fillcolor('silver')
moon_pencil.pendown()
moon_pencil.begin_fill()
moon_pencil.circle(70)
moon_pencil.end_fill()
for i in range(5):
    moon_pencil.penup()
    moon_pencil.setposition(random.randrange(25, 50), random.randrange(400, 500))
    moon_pencil.pendown()
    moon_pencil.fillcolor('dark gray')
    moon_pencil.begin_fill()
    moon_pencil.circle(random.randrange(3, 10))
    moon_pencil.end_fill()
moon_pencil.hideturtle()



wn.exitonclick()
