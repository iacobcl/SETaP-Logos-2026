import turtle
t = turtle.Turtle()
t.color("black", "white")
t.pensize(5)

def drawH():#

    # Draw the left vertical bar
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)

    # Draw the bridge
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)

    # Draw the right vertical bar
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)

    # Complete the bridge and bottom
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)

turtle.done()