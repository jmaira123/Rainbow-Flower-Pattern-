import turtle 
import colorsys 

# Setup the screen
t = turtle.Turtle()
t.speed(0)
turtle.Screen().bgcolor("black")

# Set color mode for RGB values
turtle.colormode(255)

# Function to draw the flower pattern
def draw_flower():
    t.width(2)
    num_circles = 36
    hue = 0

    for i in range(num_circles):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(int(color[0]*255), int(color[1]*255), int(color[2]*255))
        t.circle(100)
        t.right(10)
        hue += 1 / num_circles

# Call the function to draw the flower
draw_flower()

# End drawing
turtle.done()