import turtle

t = turtle.Turtle()

turtle.bgcolor('black')
t.pencolor('#f73487' )
t.right(90)
t.speed(1000)
#t.pensize(3)

a = 300     #1
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 8

t.left(3)	
a = 252       #2
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 3
	
t.left(3)
a = 230       #3
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 2
	
t.left(3)
a = 216        #4
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 0.5
	
t.left(3)
a = 213      #5
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 0
	
t.left(3)
a = 216     #6
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 1
	
t.left(3)
a = 225  #7
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 1.5
	
t.left(3)
a = 236  #8
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 1
			
t.left(3)
a = 242  #9
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 0.5

t.left(3)
a = 245  #10
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 0	
	
t.left(3)
a = 245  #11
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 0.5	
	
t.left(3)
a = 240  #12
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 1
	
t.left(3)
a = 234  #13
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 1
	
t.left(3)
a = 224  #14
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 1
	
t.left(3)
a = 212  #15
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 2
	
t.left(3)
a = 190   #16
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 3
	
t.left(3)
a = 163  # 17
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 4

t.left(3)
a = 135  #18
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 5
	
t.left(3)
a = 95  #19
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 6
	
t.left(3)
a = 65  #20
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 3

#partition
t.goto(0,0)
t.left(6)
a = 47  #20
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 3

t.left(3)
a = 65  #19
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 6	
	
t.left(3)
a = 95  #18
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 5
	
t.left(3)
a = 135  # 17
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 4
	
t.left(3)
a = 163  #16
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 3	
			
t.left(3)
a = 190 #15
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 2				
					
t.left(3)
a = 212  #14
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 1						

t.left(3)
a = 224  #13
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 1

t.left(3)
a = 234  #12
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 1	
									
t.left(3)
a = 240  #11
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 0.5	
	
t.left(3)
a = 245  #10
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 0															

t.left(3)
a = 245  #9
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 0.5														
	
t.left(3)
a = 242  #8
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 1																
t.left(3)
a = 236  #7
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 1.5	
	
t.left(3)
a = 225     #6
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 1															
	
t.left(3)
a = 216      #5
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a -= 0
	
t.left(3)
a = 213        #4
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 0.5														
	
t.left(3)
a = 216       #3
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 2															

t.left(3)	
a = 230       #2
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 3									

t.left(3)
a = 252    #1
for i in range(6):
	t.fd(a)
	t.backward(a)
	t.left(1)
	a += 8																											
																																																																																	
turtle.done()