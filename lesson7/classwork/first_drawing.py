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
t.goto(50, -50)
t.pendown()

for i in range(4):
  t.forward(200)
  t.left(90)