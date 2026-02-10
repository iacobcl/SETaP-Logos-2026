import turtle

def draw_logo_with_smaller_s():
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Masonic Compass with S")
    
    # Turtle setup
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.hideturtle()
    t.pensize(3)

    def jump_to(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    # --- Draw the Compass ---
    def draw_compass():
        # 1. Hinge (Outer Circle)
        t.pensize(5)
        jump_to(0, 130) 
        t.setheading(0)
        t.circle(25) 
        
        # 2. Hinge (Inner Circle)
        jump_to(0, 145)
        t.circle(10)
        
        t.pensize(3) # Reset pen size for legs

        # 3. Left Leg
        jump_to(-22, 140)
        t.setheading(245) # Angle down-left
        t.forward(240)    # Outer long leg
        
        # Sharp point & inner leg
        t.left(165)
        t.forward(190)    # Up inner leg
        
        # 4. Right Leg
        jump_to(22, 140)
        t.setheading(295) # Angle down-right
        t.forward(240)    # Outer long leg
        
        # Sharp point & inner leg
        t.right(165)
        t.forward(190)    # Up inner leg

    # --- Draw the 'S' ---
    def draw_letter_s():
        # Move to the center space
        # Y=35 positions it slightly higher in the wider part of the gap
        jump_to(0, 60) 
        
        t.write("S", align="center", font=("Times New Roman", 50, "bold"))

    # Execute drawing
    draw_compass()
    draw_letter_s()

    screen.mainloop()

if __name__ == "__main__":
    draw_logo_with_smaller_s()