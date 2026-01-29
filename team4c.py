import turtle
t = turtle.Turtle()

t.pensize(5)
t.speed(5)

def drawT(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.fillcolor("lightblue")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(85)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(85)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(15)
    t.end_fill()
    
def drawR(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.pendown()


    t.setheading(90)
    t.forward(75)


    t.right(90)
    t.forward(10)
    t.circle(-15, 180)

    t.left(120)
    t.forward(50)

    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(50)
    t.penup()

    t.goto(startx, starty)
    t.setheading(180)
    t.pendown()
    t.forward(10)


    t.right(90)
    t.forward(85)
    t.right(90)
    t.forward(20)
    t.circle(-25, 165)
    
def drawH(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(360)
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
    
    
def drawF(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(360)
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

def drawHanger(startx, starty):
    
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(90)   
    t.forward(50)      
    t.circle(45, 230)  
    

    t.pensize(5)      
    
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(205) 
    t.forward(320)     
    
    t.setheading(0)   
    t.forward(60)     
    
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(335) 
    t.forward(320)     
    t.setheading(180)  
    t.forward(60)
    
    
drawT(-500, 100)
drawH(-400, 100)
drawR(-300, 100)
drawF(-100, 100)
drawT(0, 100)