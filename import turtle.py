import turtle

def mid_top():
    t.penup()
    t.home()
    t.left(90)
    t.forward(200)
    t.pendown()

def left_shield(): 
    mid_top()
    t.left(215)
    t.circle(150, 90)
    
    t.right(105) 
    t.circle(-350, 90)
    
    

def right_shield():
    mid_top()
    t.right(215)
    t.circle(-150, 90)
    
    t.left(105) 
    t.circle(350, 90)

#to test where middle line is
def test_middle():
    mid_top()
    t.right(180)
    t.forward(600)


def sheild():
    test_middle()
    left_shield()
    right_shield()



screan = turtle.Screen()
t = turtle.Turtle()

sheild()
turtle.done()
