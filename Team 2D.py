import turtle

#Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(8)

#Helper function for circles
def draw_circle(radius, color):
    t.pencolor(color)
    t.circle(radius)
