import turtle
w = turtle.Screen()
w.clear()
w.bgcolor("#ffffff")
screen = turtle.Screen()
t = turtle.Turtle()

#turtle.tracer(0, 0)
t.speed(20)
t.penup()
t.width(1)
t.goto(0,0)
t.seth(0)
t.pencolor("#002FA6")
t.pendown()
x=5
for x in range(120):
	x=x+1
	if x%2==0:
		t.pencolor("#FF1900")
	else:
		t.pencolor("#FFEA00")
	for x in range(4):
		t.forward(100)
		t.left(90)
	t.left(x)
w.exitonclick()
