import turtle
import random


def negyzet():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def pont(x,y):
    turtle.goto(x,y)
    turtle.dot(10, "black")


def dobas():
    turtle.clear()
    turtle.hideturtle()
    negyzet()
    szam = random.randint(1, 6)
    turtle.penup()

    if szam == 1:
        pont(0,0)
    elif szam == 2:
        pont(-30,30)
        pont(30, -30)
    elif szam == 3:
        pont(-30,30)
        pont(30, -30)
        pont(0,0)


ablak = turtle.Screen()

turtle.onkey(dobas, "n")
turtle.onkey(turtle.bye, "Escape")

turtle.listen()
turtle.mainloop()