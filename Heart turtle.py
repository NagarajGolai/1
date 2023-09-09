import turtle

t = turtle.Turtle()

t.penup()
t.goto(0,-200)
t.pencolor('red')
t.pendown()

t.fillcolor('red')
t.begin_fill()
t.left(47)
t.fd(300)

for i in range(20):
	t.left(10)
	t.fd(21)
	
t.right(135)

for i in range(20):
	t.fd(20)
	t.left(10)
	
t.fd(310)
t.end_fill()

t.penup()
t.goto(-200,-160)
t.left(47+40)
t.pendown()

t.pensize(10)
t.fd(550)
t.pensize(1)

t.begin_fill()
t.left(90)
t.fd(25)
for j in range(3):
	t.right(120)
	t.fd(50)

t.end_fill()

t.hideturtle()
turtle.done()