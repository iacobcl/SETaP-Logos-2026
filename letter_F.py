#Created File
import turtle
# #screen setup
# screen = turtle.Screen()
# screen.bgcolor("white")

t = turtle.Turtle()
t.speed(1)
t.pencolor("black")
t.pensize(5)



#function to draw a F letter
def draw_F():
    #drawing straight F
    t.left(90)
    t.forward(100)
    #drawing top horizontal line
    t.right(90)
    t.forward(70)
    #go down
    t.right(90)
    t.forward(20)
    #drawing middle horizontal line
    t.right(90)
    t.forward(50)
    #go back to vertical line
    t.left(90)
    t.forward(20)
    #drawing bottom horizontal line
    t.left(90)
    t.forward(40)
    #go down
    t.right(90)
    t.forward(20)
    #drawing bottom horizontal line
    t.right(90)
    t.forward(40)
    #return to starting position
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)

draw_F()

turtle.done()