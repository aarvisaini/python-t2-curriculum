# Problem 1
# Use turtle to draw a filled square inside a larger square.
import turtle

t = turtle.Turtle()
t.speed(8)
t.color("hot pink")
t.begin_fill()
for i in range(4):
  t.forward(100)
  t.left(90)
t.end_fill()

t.penup()
t.goto(-50, -50)
t.pendown()

for i in range(4):
  t.forward(200)
  t.left(90)
t.done  
  
# Problem 2
# Use turtle to draw a flower with 6 petals.
# Each petal can be made using a small circle arc.

import turtle

t = turtle.Turtle()
t.speed(8)

t.color("cyan")
t.begin_fill()
for i in range(6):
  t.circle(50, 60)
  t.left(120)
  t.circle(50, 60)
  t.right(60)
  t.left(120)
t.end_fill()  



# Problem 3
# Use turtle to draw a rainbow:
# Draw 5 semicircles with different colors, each one bigger than the last.



# Problem 4
# Use turtle to draw a grid of 3x3 small squares.
import turtle
t = turtle.Turtle()
t.speed(6)
t.width(5)
t.color("pink")
for i in range(4):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(-50, -0)  
t.pendown()
for i in range(4):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(-100, -0)  
t.pendown()
for i in range(4):
    t.forward(50)  
    t.right(90)
t.penup()
t.goto(-100, 50)  
t.pendown()
for i in range(4):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(-49, 50)  
t.pendown()
for i in range(3):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(-0, -0)  
t.pendown()
for i in range(3):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(-50, 50)  
t.pendown()
for i in range(4):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(-0, 50)  
t.pendown() 
for i in range(4):
       t.forward(50)  
       t.right(90)
t.penup()
t.goto(50, 50)  
t.pendown() 
for i in range(4):
       t.forward(50)  
       t.right(90)
t.done()       


# Problem 5
# Use turtle to make a simple "logo" using at least 3 different colors and 2 shapes.
import turtle
t = turtle.Turtle()
t.speed(3)
t.color("black")
t.width(10)
t.circle(51)
t. penup ()
t.goto(-50,-70)
t.pendown()
t.color("yellow")
t.width(10)
t.circle(50)
t.penup()
t.goto(57,-71)
t.pendown()
t.color("green")
t.circle(50)
t.penup()
t.goto(-111, -2)
t.pendown()
t.color("royal blue")
t.circle(50)
t.penup()
t.goto(110, 2)
t.pendown()
t.color("red")
t.circle(50)
t.done()