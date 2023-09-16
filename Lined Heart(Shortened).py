import turtle

t = turtle.Turtle()

turtle.bgcolor('black')
t.pencolor('#f73487' )
t.right(90)
t.speed(1000)

a_list = [300,252,230,216,213,216,225,236,242,245,245,240,234,224,212,190,163,135,95,65]

a1_list = [-8, -3, -2, -0.5, 0, 1, 1.5, 1, 0.5, 0, -0.5, -1, -1, -1, -2, -3, -4, -5, -6, -3]


for a , a1 in zip( a_list , a1_list ):
	for i in range(6):
		t.fd(a)
		t.backward(a)
		t.left(1)
		a += a1
	t.left(3)

a_list.append(47)
a_list.remove(300)	
b_list = a_list[:: -1]
a2_list =  [-x if x > 0 else abs(x) for x in a1_list]
b1_list = a2_list[:: -1]
#print(b_list)  --> prints 'None'
#print(a_list) ----> prints reversed list


t.goto(0,0)
t.left(3)

for b , b1 in zip( b_list , b1_list):
	for i in range(6):
		t.fd(b)
		t.backward(b)
		t.left(1)
		b += b1
	t.left(3)



turtle.done()