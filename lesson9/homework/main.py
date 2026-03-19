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