import turtle
import math

# Making screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Nimed")
screen.setup(width=1000, height=600)

# Turtle lol
pen = turtle.Turtle()
pen.color("yellow")
pen.pensize(2)
pen.hideturtle()
pen.color("yellow")
pen.speed(0)

def draw_block(x, y,width,height, type, r): # Magic Machine - DO NOT BRAKE!!!
    #How to use THE MACHINE!
    #   Machine request from you to enter 5 numbers
    #   1. x-cord
    #   2. Y-cord
    #   3. width
    #       Practicaly always use as object wide
    #   4. width
    #   5. height
    #       Always used as object wide
    #   6. type
    #       The most important part, with type you sellect a object drawning type
    #       Type list: circle, split_circle_w,split_circle_w_neg, split_circle_h, split_circle_h_neg, slope, neg-slope, rectang
    #   7. r
    #       Practicaly never use, but need for circles
  
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    if type == "circle": # Make full circles
    # How to use?:
    #   Make a full circle with (x,y) and radius(r)
    #   (x,y) = are left outer part of circle
    #   r = is a radius lol
        pen.circle(r)
    elif type == "split_circle_w": # Split circles (R,D,S,...)
    # How to use?:
    #   Make a half circle with (x,y) and radius(r)
    #   (x,y) = are left outer part of circle
    #   widht = is diference betewen iner- and outer- radius
    # r= is a radius wow...
        pen.circle(r,180)
        pen.left(90)
        pen.forward(width)
        pen.right(180+90+180)
        pen.circle(r-width,-180)

    elif type == "split_circle_w_neg": # Split circles (R,D,S,...)
    # How to use?:
    #   Make a OTHER-half circle with (x,y) and radius(r)
    #   (x,y) = are left outer part of circle
    #   widht = is diference betewen iner- and outer- radius
    # r= is a radius wow...
        pen.left(180)
        pen.circle(r,180)
        pen.left(90)
        pen.forward(width)
        pen.right(180+90+180)
        pen.circle(r-width,-180)
    
    elif type == "split_circle_h": # Split circles (U,A,O,...)
    #How to use?:
    #   Make a half circle with (x,y) and radius(r)
    #   (x,y) = are left outer part of circle
    #   widht = is diference betewen iner- and outer- radius
    # r= is a radius wow...
        pen.right(90)
        pen.circle(r,180)
        pen.left(90)
        pen.forward(width)
        pen.right(180+90+180)
        pen.circle(r-width,-180)
        pen.left(90)
    
    elif type == "split_circle_h_neg": # Split circles (S,...)
    #How to use?:
    #   Make a OTHER half circle with (x,y) and radius(r)
    #   (x,y) = are left outer part of circle
    #   widht = is diference betewen iner- and outer- radius
    # r= is a radius wow...
        pen.left(90)
        pen.circle(r,180)
        pen.left(90)
        pen.forward(width)
        pen.right(180+90+180)
        pen.circle(r-width,-180)
        pen.left(90)
    elif type == "slope": # Make slopes (R,N,M,...)
        #How to use?:
        #   make an amaizing calculated slope!
        #   (x,y) = are left outer part of the slope box
        #   widht = is a wide of the slope box
        #   height = is a slope height box
        #       HOW THAT WORK???
        #       Slope automaticly calculate own lenght and angle, from you only requiers enter slope box
        #       Important to say, that slope thiknes is constant
        #   IF SLOPE ISN't MATCH, USE DIF SLOPE TYPE
        diagonal = math.sqrt(width**2 + height**2)
        angle = math.degrees(math.atan2(height, width))
        width_line =10
        for _ in range(2):
            pen.forward(width_line)
            pen.right(angle)
            pen.forward(diagonal)
            pen.right(180-angle)
    elif type == "neg-slope": # Make revers slopes (M,V,Y...)
        #How to use?:
    #   make an amaizing calculated slope!
    #   (x,y) = are left outer part of the slope box
    #   widht = is a wide of the slope box
    #   height = is a slope height box
    #       HOW THAT WORK???
    #       Slope automaticly calculate own lenght and angle, from you only requiers enter slope box
    #       Important to say, that slope thiknes is constant
    #   IF SLOPE ISN't MATCH, USE DIF SLOPE TYPE
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
    elif type == "rectang": # Make rectangels
    #How to use?:
    #   make an rec!
    #   (x,y) = are left outer part of the rec
    #   widht = is a wide of the rec
    #   height = is a rec height
        for _ in range(2):
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)
    pen.end_fill()

def draw_T(x, y): # T
    draw_block(x, y, 60, 10, "rectang", 0)
    draw_block(x+25, y-10, 10, 60, "rectang", 0)

def draw_I(x, y): # I
    draw_block(x + 20, y-10, 10, 60, "rectang", 0)
    draw_block(x + 25, y-5, 0, 0, "circle", 5)

def draw_M(x, y): # M
    draw_block(x, y, 10, 70, "rectang", 0)
    draw_block(x, y, 30, 60, "slope", 0)
    draw_block(x+30, y, 30, 60, "neg-slope", 0)
    draw_block(x+60, y, 10, 70, "rectang", 0)

def draw_U(x, y): # U
    draw_block(x, y, 10, 40, "rectang", 0)
    draw_block(x, y-40, 10, 30, "split_circle_h", 30)
    draw_block(x+50, y, 10, 70, "rectang", 0)

def draw_R(x, y): # R
    draw_block(x, y, 10, 70, "rectang", 0)
    draw_block(x, y, 30, 10, "rectang", 0)
    draw_block(x, y-30, 30, 10, "rectang", 0)
    draw_block(x+30, y-40, 10, 20, "split_circle_w", 20)
    draw_block(x, y-30, 40, 40, "slope", 0)

def draw_S(x,y): # S
    draw_block(x, y-60, 30, 10, "rectang", 0)
    draw_block(x+30, y-70, 10, 20, "split_circle_w", 20)
    draw_block(x+10, y-30, 20, 10, "rectang", 0)
    draw_block(x+10, y, 10, 20, "split_circle_w_neg", 20)
    draw_block(x+40, y-10, 30, 10, "rectang", 0)

def draw_A(x,y): # A
    draw_block(x,y-30, 10, 20, "split_circle_h_neg", 20)

def draw_name_TIMUR(): #Here I request and align letters
    start_x = -200
    y = 50
    spacing = 50
    draw_T(start_x, y)
    draw_I(start_x + 10 + spacing*1, y)
    draw_M(start_x + 10 + spacing*2, y)
    draw_U(start_x + 50 + spacing*3, y)
    draw_R(start_x + 80 + spacing*4, y)
    draw_A(start_x + 150 + spacing*5, y)

draw_name_TIMUR()

turtle.done()