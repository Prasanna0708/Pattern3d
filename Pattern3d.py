import turtle as t

t.speed(0)
t.tracer(10)
t.bgcolor('black')

color = ('red','green','blue','yellow','orange','cyan','coral')     #seven colors

for i in range(250):
    t.pencolor(color[i%7])
    t.pensize(2)
    t.fd(i*1)
    t.rt(100)
    t.circle(60,120)
    t.right(90)
