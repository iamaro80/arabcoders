import turtle
import time

def draw_square():
    window = turtle.Screen()
    window.bgcolor('black')
    brad = turtle.Turtle()
    brad.shape('circle')
    brad.color('red','green')
    brad.speed(1)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    # count = 25
    # while count > 0:
    #     count -= 1
    #     print count
    #     brad.right(75)
    #     brad.forward(100)
    #     brad.right(90)
    #     brad.forward(100)
    #     brad.right(90)
    #     brad.forward(100)
    #     brad.right(90)
    #     brad.forward(100)


    window.exitonclick()

draw_square()
