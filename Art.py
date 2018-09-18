# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 36 hexagons, each 10 degrees apart
for n in range(36):
# make hexagon by repeating 6 times
    for i in range(6):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(100)
        shelly.left(60)
    # add a turn before the next hexagon
    shelly.right(10)

# get ready to draw 36 circles
shelly.penup()
shelly.color('white')
# repeat 36 times to match the 36 hexagons
for i in range(36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)
# hide turtle to finish the drawing
shelly.hideturtle()
