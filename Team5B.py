from turtle import Turtle, Screen

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

if __name__ == "__main__": # This block will only run if this file is executed directly
    good_boy = Turtle()
    square(good_boy, 100)
    Screen().mainloop()