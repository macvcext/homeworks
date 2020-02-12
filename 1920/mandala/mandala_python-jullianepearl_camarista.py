import turtle

window = turtle.Screen()
window.bgcolor("Dimgray")
t = turtle.Turtle()

t.speed(0)
t.pencolor("light blue")
t.pensize(2)
h = 30

for j in range(18):

    for i in range(5):
        t.forward(h)
        t.right(75)

    t.forward(15)
    t.right(5)


t.penup()
t.pendown()
t.pencolor("darkgray")
t.pensize(3)
h = 50
a = 15

for j in range(25):

    for i in range(3):
        t.forward(h)
        t.left(120)
    t.forward(15)
    t.right(a)

t.penup()
t.backward(150)
t.left(45)
t.pendown()
t.pencolor("powderblue")
t.pensize(4)

h = 200

for j in range(18):

    for i in range(5):
        t.forward(h)
        t.right(75)

    t.forward(20)
    t.right(5) 

t.penup()
t.left(300)
t.right(95)
t.back(105)
t.right(30)
t.pendown()
t.pencolor("darkgray")
t.pensize(10)
t.circle(200)


turtle.exitonclick()


#reference: https://github.com/LekkerPrutsen/Spirograph-with-turtle/commits?author=LekkerPrutsen

