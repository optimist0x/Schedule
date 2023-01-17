import turtle

# Create a turtle object
t = turtle.Turtle()

# Use a for loop to draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Keep the window open until the user clicks
turtle.exitonclick()
