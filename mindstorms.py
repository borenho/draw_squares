import turtle     # Module used to do the drawing

def lets_draw():
	# Create canvas to draw the square on
	window = turtle.Screen()
	window.bgcolor("pink")

	# Make the drawing
	brad = turtle.Turtle()    # Instantiate brad
	# Customize brad
	brad.shape("turtle")
	brad.color("green")
	brad.speed(2)

	brad.forward(100)    # Move him forwad 100 steps
	brad.right(90)    # Turn right 90 degrees

	brad.forward(100)    # Move him forwad 100 steps
	brad.right(90)    # Turn right 90 degrees

	brad.forward(100)    # Move him forwad 100 steps
	brad.right(90)    # Turn right 90 degrees

	brad.forward(100)    # Move him forwad 100 steps
	brad.right(90)    # Turn right 90 degrees

	window.exitonclick()

# Make sure to call the function
lets_draw()