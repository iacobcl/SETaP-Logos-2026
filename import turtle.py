import turtle

# ================= CONTROLS =================
CENTER_X = 0
CENTER_Y = 0

SHIELD_X = -21
SHIELD_Y = 20

SWORD_X = 0
SWORD_Y = 0

DUMBBELL_X = -50
DUMBBELL_Y = 5

SHIELD_HEIGHT = 190
SWORD_LENGTH = 450
DUMBBELL_LENGTH = 500
HANDLE_LENGTH = 40


# ================= SHIELD =================
def mid_top(divider):
    t.penup()
    t.goto(SHIELD_X + CENTER_X, SHIELD_Y + CENTER_Y)
    t.setheading(90)
    t.forward(SHIELD_HEIGHT // max(divider, 1))
    t.pendown()


def left_shield(divider):
    top_divider = divider / 1.1 if divider != 0 else 1
    bottom_angle = divider / 1.15 if divider != 0 else 1

    mid_top(divider)
    t.left(215)
    t.circle(150 // top_divider, 90)

    t.right(105)
    t.circle(-350 // max(divider, 1), 90 * bottom_angle)


def right_shield(divider):
    top_divider = divider / 1.1 if divider != 0 else 1
    bottom_angle = divider / 1.15 if divider != 0 else 1

    mid_top(divider)
    t.right(215)
    t.circle(-150 // top_divider, 90)

    t.left(105)
    t.circle(350 // max(divider, 1), 90 * bottom_angle)


def sheild():
    t.color("blue")
    t.begin_fill()
    left_shield(0)
    right_shield(0)
    t.end_fill()
    
    t.color("skyblue")
    t.begin_fill()
    left_shield(1.2)
    right_shield(1.2)
    t.end_fill()
    mid_top(1)


# ================= SWORD =================
def draw_straight_blade():
    t.penup()
    t.goto(140 + SWORD_X + CENTER_X, 180 + SWORD_Y + CENTER_Y)
    t.pendown()

    t.color("silver")
    t.begin_fill()
    t.setheading(225)
    t.forward(SWORD_LENGTH)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.forward(SWORD_LENGTH)
    t.left(90)
    t.forward(35)
    t.end_fill()

    t.penup()
    t.goto(140 + SWORD_X + CENTER_X, 180 + SWORD_Y + CENTER_Y)
    t.setheading(225)
    t.forward(SWORD_LENGTH)
    t.pendown()

    t.begin_fill()
    t.left(20)
    t.forward(50)
    t.left(140)
    t.forward(60)
    t.end_fill()


def draw_guard():
    t.penup()
    t.goto(140 + SWORD_X + CENTER_X, 180 + SWORD_Y + CENTER_Y)
    t.setheading(225)
    t.left(90)
    t.forward(17.5)
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
    t.penup()
    t.goto(140 + SWORD_X + CENTER_X, 180 + SWORD_Y + CENTER_Y)
    t.setheading(225)
    t.left(90)
    t.forward(22.5)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.setheading(45)
    t.forward(HANDLE_LENGTH)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(HANDLE_LENGTH)
    t.left(90)
    t.forward(10)
    t.end_fill()

    t.penup()
    t.setheading(45)
    t.forward(HANDLE_LENGTH)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(10)
    t.end_fill()


# ================= DUMBBELL =================
def draw_dumbbell_bar():
    t.penup()
    t.goto(-140 + DUMBBELL_X + CENTER_X, 180 + DUMBBELL_Y + CENTER_Y)
    t.pendown()

    t.color("gray")
    t.begin_fill()
    t.setheading(315)
    t.forward(DUMBBELL_LENGTH)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(DUMBBELL_LENGTH)
    t.right(90)
    t.forward(20)
    t.end_fill()


def draw_dumbbell_weights():
    # Top-left outer
    t.penup()
    t.goto(-140 + DUMBBELL_X + CENTER_X, 180 + DUMBBELL_Y + CENTER_Y)
    t.setheading(315)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()

    t.color("darkgray")
    t.begin_fill()
    t.forward(25)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(80)
    t.end_fill()

    # Top-left inner
    t.penup()
    t.goto(-140 + DUMBBELL_X + CENTER_X, 180 + DUMBBELL_Y + CENTER_Y)
    t.setheading(315)
    t.forward(55)
    t.left(90)
    t.forward(35)
    t.right(90)
    t.pendown()

    t.color("dimgray")
    t.begin_fill()
    t.forward(15)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(90)
    t.end_fill()

    # Bottom-right outer
    t.penup()
    t.goto(-140 + DUMBBELL_X + CENTER_X, 180 + DUMBBELL_Y + CENTER_Y)
    t.setheading(315)
    t.forward(DUMBBELL_LENGTH - 70)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()

    t.color("darkgray")
    t.begin_fill()
    t.forward(25)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(80)
    t.end_fill()

    # Bottom-right inner
    t.penup()
    t.goto(-140 + DUMBBELL_X + CENTER_X, 180 + DUMBBELL_Y + CENTER_Y)
    t.setheading(315)
    t.forward(DUMBBELL_LENGTH - 85)
    t.left(90)
    t.forward(35)
    t.right(90)
    t.pendown()

    t.color("dimgray")
    t.begin_fill()
    t.forward(15)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(90)
    t.end_fill()


# ================= RUN =================
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

sheild()
draw_dumbbell_bar()
draw_dumbbell_weights()
draw_straight_blade()
draw_guard()
draw_handle()

turtle.done()
