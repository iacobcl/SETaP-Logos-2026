from turtle import Turtle

def square(turtle, side_length):
    turtle.pendown()
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.penup()

if __name__ == "__main__":
    good_boy = Turtle()
    square(good_boy, 100)