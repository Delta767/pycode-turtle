import turtle
w = turtle.Screen()
w.clear()
w.bgcolor("#ffffff")
screen = turtle.Screen()
t = turtle.Turtle()

t.speed(20)
t.pendown()
for x in range(648):
	if x%5==0:
		t.color("#FF0000")
	elif x%5==1:
		t.color("#FF6A00")
	elif x%5==2:
		t.color("#FFD500")
	elif x%5==3:
		t.color("#FFBB00")
	elif x%5==4:
		t.color("#FF5900")
	t.forward(x)
	t.left(107)
	x=x+1
t.forward(150)
w.exitonclick()
