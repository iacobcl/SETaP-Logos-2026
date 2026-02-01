import turtle

def mid_top(divider):
    t.penup()
    t.home()
    t.left(90)
    t.forward(200//divider)
    t.pendown()

def left_shield(divider):
    top_divider = divider/1.1
    bottom_angle = divider/1.15
    
    if divider == 0:
        divider = 1
        top_divider = 1
        bottom_angle = 1
        
    mid_top(divider)
    t.left(215)
    print(top_divider)
    t.circle(150//top_divider, 90)
    
    t.right(105) 
    t.circle(-350//divider, 90*bottom_angle)
    
    

def right_shield(divider):
    top_divider = divider/1.1
    bottom_angle = divider/1.15
    
    if divider == 0:
        divider = 1
        top_divider = 1
        bottom_angle = 1
        
    mid_top(divider)
    t.right(215)
    print(top_divider)
    t.circle(-150//top_divider, 90)
    
    t.left(105) 
    t.circle(350//divider, 90*bottom_angle)

#to test where middle line is
def test_middle():
    mid_top(1)
    t.right(180)
    t.forward(600)


def sheild():
    #test_middle()
    left_shield(0)
    left_shield(1.2)
    right_shield(0)
    right_shield(1.2)
    mid_top(1)

def draw_straight_blade():
    """Draw blade correctly"""
    t.penup()
    t.goto(140, 180)
    t.pendown()
    
    # Blade body
    t.color("silver")
    t.begin_fill()
    t.setheading(225)
    t.forward(450)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.forward(450)
    t.left(90)
    t.forward(35)
    t.end_fill()
    
    # Sharp point
    t.penup()
    t.goto(140, 180)
    t.setheading(225)
    t.forward(450)
    # Start at left corner
    t.pendown()
    t.color("silver")
    t.begin_fill()
    # Left edge line to tip
    t.left(20)
    t.forward(50)
    # Right edge line back to right corner
    t.left(140)
    t.forward(60)
    t.end_fill()

def draw_guard():
    """Cross-guard"""
    t.penup()
    t.goto(140, 180)
    t.setheading(225)
    t.left(90)
    t.forward(17.5)  # Move to center of blade
    t.pendown()
    
    t.color("gold")
    t.begin_fill()
    t.setheading(135)
    t.forward(40)
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(12)
    t.end_fill()

def draw_handle():
    """Handle and pommel"""
    t.penup()
    t.goto(140, 180)
    t.setheading(225)
    t.left(90)
    t.forward(17.5)  # Move to center of blade
    t.pendown()
    
    t.color("black")
    t.begin_fill()
    t.setheading(45)
    t.forward(70)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(10)
    t.end_fill()
    
    # Pommel
    t.penup()
    t.goto(140, 180)
    t.setheading(225)
    t.left(90)
    t.forward(17.5)  # Move to center of blade
    t.setheading(45)
    t.forward(70)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

screan = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

sheild()
draw_straight_blade()
draw_guard()
draw_handle()
turtle.done()
