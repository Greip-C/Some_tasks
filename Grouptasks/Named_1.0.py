import turtle
import math

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Nimed")
screen.setup(width=1000, height=600)

pen = turtle.Turtle()
pen.color("yellow")
pen.speed(0)

def draw_block(x, y,width,height, type, r):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    if type == "circle":
        pen.circle(r)
    elif type == "split_circle_w":
        pen.circle(r,180)
        pen.left(90)
        pen.forward(width)
        pen.right(180+90+180)
        pen.circle(r-width,-180)
    elif type == "split_circle_h":
        pen.right(90)
        pen.circle(r,180)
        pen.left(90)
        pen.forward(width)
        pen.right(180+90+180)
        pen.circle(r-width,-180)
        pen.left(90)
    elif type == "slope":
        diagonal = math.sqrt(width**2 + height**2)
        angle = math.degrees(math.atan2(height, width))
        width_line =10
        for _ in range(2):
            pen.forward(width_line)
            pen.right(angle)
            pen.forward(diagonal)
            pen.right(180-angle)
    elif type == "neg-slope":
        diagonal = math.sqrt(width**2 + height**2)
        angle = math.degrees(math.atan2(height, width))
        width_line =10
        pen.end_fill()
        pen.penup()
        pen.goto(x, y-height)
        pen.pendown()
        pen.begin_fill()
        for _ in range(2):
            pen.forward(width_line)
            pen.left(angle)
            pen.forward(diagonal)
            pen.left(180-angle)
    elif type == "rectang":
        for _ in range(2):
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)
    pen.end_fill()

# Täht T
def draw_T(x, y):
    draw_block(x, y, 60, 10, "rectang", 0)
    draw_block(x+25, y-10, 10, 60, "rectang", 0)

# Täht I
def draw_I(x, y):
    draw_block(x + 20, y-10, 10, 60, "rectang", 0)
    draw_block(x + 25, y-5, 0, 0, "circle", 5)

# Täht M
def draw_M(x, y):
    draw_block(x, y, 10, 70, "rectang", 0)
    draw_block(x, y, 30, 60, "slope", 0)
    draw_block(x+30, y, 30, 60, "neg-slope", 0)
    draw_block(x+60, y, 10, 70, "rectang", 0)

# Täht U
def draw_U(x, y):
    draw_block(x, y, 10, 40, "rectang", 0)
    draw_block(x, y-40, 10, 30, "split_circle_h", 30)
    draw_block(x+50, y, 10, 70, "rectang", 0)
    #draw_block(x + 50, y - 70, 10, 60)
    #draw_block(x + 10, y - 10, 40, 10)

# Täht R
def draw_R(x, y):
    draw_block(x, y, 10, 70, "rectang", 0)
    draw_block(x, y, 30, 10, "rectang", 0)
    draw_block(x, y-30, 30, 10, "rectang", 0)
    draw_block(x+30, y-40, 10, 20, "split_circle_w", 20)
    draw_block(x, y-30, 40, 40, "slope", 0)


# Funktsioon nime kirjutamiseks
def draw_name_TIMUR():
    start_x = -200
    y = 50
    spacing = 50

    draw_T(start_x, y)
    draw_I(start_x + 10 + spacing*1, y)
    draw_M(start_x + 10 + spacing*2, y)
    draw_U(start_x + 50 + spacing*3, y)
    draw_R(start_x + 80 + spacing*4, y)

pen.pensize(2)
pen.hideturtle()
pen.color("yellow")
pen.speed(0)

draw_name_TIMUR()

turtle.done()
