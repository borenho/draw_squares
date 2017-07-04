import turtle

def draw_art():
	window = turtle.Screen()
	window.bgcolor("skyblue")

	# Create turtle earth to draw cicular fractals
	earth = turtle.Turtle()
	earth.shape("turtle")
	earth.color("blue")
	earth.speed(5)

	for i in range(36):
		earth.right(10)
		earth.circle(100)

	window.exitonclick()

draw_art()
