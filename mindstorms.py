import turtle     # Module used to do the drawing

def draw_square(some_turtle):
	for i in range(4):
		some_turtle.forward(150)    # Move him forwad 100 steps
		some_turtle.right(90)    # Turn right 90 degrees

def draw_triangle(some_turtle):
	for i in range(3):
		some_turtle.backward(200)    # Move him backwards 100 steps
		some_turtle.left(120)    # Turn right 45 degrees

def draw_art():
	# Create canvas to draw the square on
	window = turtle.Screen()
	window.bgcolor("pink")

	# Create turtle brad to draw square
	brad = turtle.Turtle()    # Instantiate brad
	# Customize brad
	brad.shape("turtle")
	brad.color("green")
	brad.speed(3)
	# Call brad
	draw_square(brad)

	# Create turtle angie to draw circle
	angie = turtle.Turtle()    # Instantiate brad
	# Customize angie
	angie.shape("arrow")
	angie.color("grey")
	angie.speed(5)
	angie.circle(100)

	# Create turtle croco to draw triangle
	croco = turtle.Turtle()    # Instantiate croco
	# Customize croco
	croco.shape("arrow")
	croco.color("blue")
	croco.speed(3)
	# Call croco
	draw_triangle(croco)
	

	window.exitonclick()

# Make sure to call the function
draw_art()