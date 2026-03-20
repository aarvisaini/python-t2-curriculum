# Problem 1
# Write a function draw_star(size) that draws a 5-point star using turtle.
# Call it.
import turtle
t = turtle.Turtle()
t.speed(8)
def draw_star(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
draw_star(100)
turtle.done()   



# Problem 3
# Draw the word "SOVA" in block letters using turtle lines.
# (It does not have to be perfect.
import turtle


t = turtle.Turtle()
t.pensize(10)
t.color("lavender")
t.speed(9)
t.penup()
t.goto(-190 ,-5)
t.pendown()

def draw_block_s():
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
draw_block_s()

t.penup()
t.goto(-110,-5)
t.pendown()

def draw_block_o(width, height):
    
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)



draw_block_o(70, 100)

t.penup()
t.goto(-15, 98)
t.pendown()


t.right(70)    
t.forward(110)


t.left(140)    
t.forward(110)


t.penup()
t.goto(-50, -50)
t.pendown()




t.penup()
t.goto(50,-5)
t.pendown()

t.left(1)
t.forward(120)


t.right(145)
t.forward(120)


t.penup()
t.backward(80) 
t.setheading(182) 
t.pendown()
t.forward(22)

turtle.done()
