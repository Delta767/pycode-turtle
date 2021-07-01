import turtle
import math
import random

w = turtle.Screen()
w.clear()
w.bgcolor("#0000FF")
t = turtle.Turtle()
#turtle.tracer(0, 0) #plots the line instantly
# - - - - -
t.speed("fastest")
amp=10
for d in range(0,360*13):
	rads=(3.1415926/180)*d
	x=math.cos(rads)*amp
	y=math.sin(rads)*amp
	#print(d, x, y)
	t.goto(x,y)
	h=hex(random.randint(0,255))
	h=h.replace("0x","")
	thecolor="#"+h+h+h
	print(h)
	t.width(10)
	t.pencolor(thecolor)
	if(d % 360==0):
		amp=amp+20
	
w.exitonclick()
# ~ t.width(5) #added
# ~ t.goto(0,0)
# ~ t.seth(0)
# ~ t.forward(100)
# ~ t.pencolor('#FF0000')
# ~ t.goto(0,0)
# ~ t.seth(90)
# ~ t.forward(100)
# ~ t.pencolor('#00FF00')
# ~ t.width(5) #added
# ~ t.goto(0,0)
# ~ t.seth(180)
# ~ t.pencolor('#0000FF')
# ~ t.forward(100)
# ~ t.penup() #added
# ~ t.goto(0,0)
# ~ t.seth(270)
# ~ t.pendown() #added
# ~ t.pencolor('#FFFF00')
# ~ t.forward(100)
# ~ t.penup() #added from now on
# ~ t.backward(300)
# ~ t.pendown()
# ~ t.circle(20,360) #t.circle(diameter?,degrees)
# ~ #turtle.update()
# ~ w.exitonclick()
# ~ #google colors; i did it


