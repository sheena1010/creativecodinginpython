# make a geometric rainbow pattern
import turtle
import random
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 64 circles, each 60 degrees apart
for n in range(256):
    shelly.color(colors[(random.randint(0,5))]) # pick color at position n
# make pentagon
    for i in range(1):
        shelly.forward(30)
        shelly.circle(10)
    # add a center shift fwd 1 each iteration and 60deg turn before the next triangle
    shelly.forward(n*1)
    shelly.right(30)
# hide turtle to finish the drawing
shelly.hideturtle()
