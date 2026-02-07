import turtle
import math


screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("white")
screen.title("Classmates Logo")


logo = turtle.Turtle()
logo.speed(0)
logo.hideturtle()

def draw_graduation_cap(x, y, size):
    """Draw a graduation cap (mortarboard)"""
    
    
    logo.penup()
    logo.goto(x, y)
    logo.pendown()
    logo.setheading(0)
    logo.fillcolor("#1E90FF")  
    logo.pencolor("#1E90FF")
    logo.begin_fill()
    
    
    logo.forward(size)
    logo.left(90)
    logo.forward(size * 0.3)
    logo.left(90)
    logo.forward(size)
    logo.left(90)
    logo.forward(size * 0.3)
    logo.left(90)
    
    logo.end_fill()
    
    
    logo.penup()
    logo.goto(x, y + size * 0.3)
    logo.pendown()
    logo.fillcolor("#4DB8FF")
    logo.begin_fill()
    
    logo.setheading(0)
    logo.forward(size)
    logo.goto(x + size + 15, y + size * 0.3 + 15)
    logo.goto(x + 15, y + size * 0.3 + 15)
    logo.goto(x, y + size * 0.3)
    
    logo.end_fill()
    
    
    logo.penup()
    logo.goto(x + size, y)
    logo.pendown()
    logo.fillcolor("#0066CC")
    logo.begin_fill()
    
    logo.goto(x + size, y + size * 0.3)
    logo.goto(x + size + 15, y + size * 0.3 + 15)
    logo.goto(x + size + 15, y + 15)
    logo.goto(x + size, y)
    
    logo.end_fill()
    
    
    logo.penup()
    logo.goto(x + size * 0.3, y - 10)
    logo.pendown()
    logo.fillcolor("#1E90FF")
    logo.begin_fill()
  
    logo.setheading(0)
    logo.forward(size * 0.4)
    logo.circle(-10, 90)
    logo.forward(20)
    logo.circle(-10, 90)
    logo.forward(size * 0.4)
    logo.circle(-10, 90)
    logo.forward(20)
    logo.circle(-10, 90)
    
    logo.end_fill()
    
    
    logo.penup()
    logo.goto(x + size + 10, y + size * 0.3 + 10)
    logo.pendown()
    logo.pencolor("#1E90FF")
    logo.pensize(3)
    logo.goto(x + size + 25, y + size * 0.3 + 35)
    
    
    logo.penup()
    logo.goto(x + size + 25, y + size * 0.3 + 30)
    logo.pendown()
    logo.fillcolor("#1E90FF")
    logo.begin_fill()
    logo.circle(5)
    logo.end_fill()
    
    logo.pensize(1)

def write_classmates_text(x, y):
    """Write 'classmates' text"""
    logo.penup()
    logo.goto(x, y)
    logo.pendown()
    logo.color("#333333")  
    
    logo.write("classmates", align="left", font=("Apple Chancery", 72, "bold"))
    
    
    logo.penup()
    logo.goto(x + 520, y + 50)
    logo.write("®", align="left", font=("Apple Chancery", 24, "normal"))


print("Drawing Classmates logo...")


draw_graduation_cap(-250, 80, 100)


write_classmates_text(-280, -50)


screen.exitonclick()