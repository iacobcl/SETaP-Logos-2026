
import turtle
t = turtle.Turtle()
t.speed(4)



#start position
t.width(5)
t.up()
t.goto(0,70)
t.circle(0,250)


#hanger
t.down()
t.circle(-20,-260)
t.circle(20,-70)
t.goto(-200,-30)
t.goto(-20,38)
t.goto(180,-30)
t.up()
t.circle(0,95)
t.down()
t.circle(15,-155)
t.up()
t.goto(-200,-30)
t.circle(0,160)
t.down()
t.circle(15,155)
t.goto(-180,-59)
t.up()
t.goto(181,-59)
t.down()
t.goto(160,-59)
t.up()

#fitcheck
t.goto(-10,-65)
t.write(
    "F i t C h e c k",
    align="center",
    font=("Brush Script MT", 45, "italic")
)
t.ht()
t.done()




