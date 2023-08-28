import turtle
import random

t= turtle.Turtle()
t.hideturtle() 
#turtle.bgcolor( 'sky blue')

#Start heading
t.penup()
t.goto(0,-600)
t.pendown()
t.write('GAME STARTS...', align = 'center')

#NAMES
name_list = ['A','B','C','D','E','F']

t.penup()
t.goto(-250,-550)
t.pendown()

for n in name_list:
	t.write(n,align = 'center',font=("",10,"normal"))
	t.penup()
	t.fd(100)
	t.pendown()


#line location
t.pensize(5)
t.penup()
t.goto(-250,-500)
t.pendown()

len_list =[]
for r in range(len(name_list)):
	a = random.randint(20, 1000)
	len_list.append(a)

for d in len_list:
	colors = ["red","blue","black","violet","cyan","magenta","green","orange","indigo"]
	c = random.choice(colors)
	t.color(c)
	colors.remove(c)
	t.left(90)
	t.fd(d)
	t.speed(5)
	t.backward(d)
	t.right(90)
	t.penup()
	t.fd(100)
	t.pendown()


#result
t.penup()
t.goto(0,500)
t.pendown()

t.color('black')

m = max(len_list) 
l = len_list.index(m)
n = name_list[l]

 
t.write(n+"("+str(m)+"mm.)"+" is the longest. It wins!",align='center',font=("Arial",12,"bold underline"))


turtle.done()