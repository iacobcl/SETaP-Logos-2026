import turtle
t = turtle.Turtle()

t.pensize(5)
t.speed(5)

def drawT(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.setheading(0)
    t.pendown()
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
    t.fillcolor("lightblue")
    t.begin_fill()

    
    t.setheading(180)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.circle(-25, 165)

    
    target_x = startx + 1.34
    target_y = starty + 55
    t.goto(target_x, target_y)


    t.setheading(300) 
    t.forward(65)
    
    t.setheading(30)  
    t.forward(10)
    
    t.setheading(120) 
    t.forward(65)
    
    t.setheading(0)  
    t.circle(15, 180) 
    
    t.forward(10)    
    t.left(90)
    t.forward(90)     

    t.end_fill()

def drawY(start_x,start_y):
    t.fillcolor("lightblue")
    t.begin_fill()
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(0)
    t.pendown()
    
   
    
    t.left(135)
    t.forward(50)

    t.left(45)
    t.forward(30)

    t.left(135)
    t.forward(60)

    t.right(45)
    t.forward(50)

    t.left(90)
    t.forward(20)

    t.left(90)
    t.forward(50)

    t.right(45)
    t.forward(60)

    t.left(135)
    t.forward(30)

    t.left(45)
    t.forward(50)

    t.goto(start_x, start_y)  
    
    t.end_fill()
    t.penup()
    t.goto(0,0)

def drawH(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(360)
    t.fillcolor("lightblue")
    t.begin_fill()
    
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)

    
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)

   
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)

   
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.end_fill()
    
    
def drawF(startx, starty):
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    t.setheading(360)
   
    t.left(90)
    t.forward(100)
   
    t.right(90)
    t.forward(70)
    
    t.right(90)
    t.forward(20)
    
    t.right(90)
    t.forward(50)
    
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.end_fill()

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
    t.forward(350)     
    
    t.setheading(0)   
    t.forward(60)     
    
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(335) 
    t.forward(350)     
    t.setheading(180)  
    t.forward(60)
    
    
drawT(-350, 100)
drawH(-230, 0)
drawR(-130, 0)
drawY(-30, 60)
drawF(30, 0)
drawT(120, 100)
drawHanger(-65, 250)
turtle.done()
