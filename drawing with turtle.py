import turtle

# creating turtle pen
pen = turtle.Turtle()
window = turtle.Screen()

# set the fillcolor
pen.fillcolor('Yellow')

# start the filling color
pen.begin_fill()

# drawing the circle of radius r
pen.up()
pen.goto(0,-120)
pen.circle(200)

# ending the fill color
pen.end_fill()

# eye1
pen.fillcolor('white')
pen.begin_fill()
pen.up()
pen.goto(-70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()
# eye1
pen.fillcolor('black')
pen.begin_fill()
pen.up()
pen.goto(-70,140)
pen.down()
pen.circle(20)
pen.end_fill()

# eye2
pen.fillcolor('white')
pen.begin_fill()
pen.up()
pen.goto(70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()

# eye2
pen.fillcolor('black')
pen.begin_fill()
pen.up()
pen.goto(70,140)
pen.down()
pen.circle(20)
pen.end_fill()

# mouth
pen.up()
pen.goto(-100,20)
pen.down()
pen.pensize(5)
pen.right(90)
pen.circle(100,180)
pen.left(90)
pen.forward(200)

# nose
pen.fillcolor('red')
pen.begin_fill()
pen.up()
pen.goto(30,80)
pen.down()
pen.right(60)
pen.forward(60)
pen.left(120)
pen.forward(60)
pen.left(120)
pen.forward(60)
pen.end_fill()



