import turtle
t = turtle.Turtle()
t.speed(20)
#start position

t.width(8)
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
t.goto(-8,-75)
t.write(
    "FitCheck",
    align="center",
    font=("Courier New", 50, "bold")
)
t.up()
t.goto(-108, -230)
t.down()
t.ht()
t.circle(230,360)




