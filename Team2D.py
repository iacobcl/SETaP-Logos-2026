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

#Center the drawing
t.penup()
t.goto(0, -120)
t.setheading(0)
t.pendown()

#Outer gold ring
t.penup()
t.goto(140, 70)     # RIGHT (+x) and UP (+y)
t.setheading(110)    # Cut at 90 degrees (top)
t.pendown()

t.width(10)
t.pencolor("#d4a23a")
t.circle(150, 340)  # 270° arc → 90° gap

#Inner navy ring (shifted + 90° cut)
t.penup()
t.goto(115, 60)     # RIGHT (+x) and UP (+y)
t.setheading(110)    # Cut at 90 degrees (top)
t.pendown()

t.width(14)
t.pencolor("#162a45")
t.circle(120, 330)  # 270° arc → 90° gap


#Leaf shape

t.penup()
t.goto(-20, -20)
t.setheading(120)
t.pendown()

t.width(3)
t.fillcolor("#7ac142")
t.begin_fill()
t.circle(100, 75)
t.setheading(-60)
t.circle(100, 75)
t.end_fill()

#Check mark
t.penup()
t.goto(85, 40)
t.setheading(-50)
t.pendown()

t.width(10)
t.pencolor("#162a45")
t.forward(40)
t.left(100)
t.forward(90)

turtle.done()