import turtle as t


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

