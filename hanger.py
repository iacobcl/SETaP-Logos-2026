import turtle as t


def drawHanger(startcoords):
 
    
    t.penup()
    t.goto(startcoords)
    t.pendown()
    t.setheading(90)   
    t.forward(50)      
    t.circle(45, 230)  
    

    t.pensize(5)      
    
    t.penup()
    t.goto(startcoords)
    t.pendown()
    t.setheading(205) 
    t.forward(320)     
    
    t.setheading(0)   
    t.forward(60)     
    
    t.penup()
    t.goto(startcoords)
    t.pendown()
    t.setheading(335) 
    t.forward(320)     
    t.setheading(180)  
    t.forward(60)      

