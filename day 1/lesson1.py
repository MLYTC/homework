from turtle import*


#we want to paint a house

# step 1:draw a square

speed(30)
width(8)
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
begin_fill()
forward(75)
color("blue")
left(90)

forward(100)
right(90)

forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)

pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(40, 120)


pendown()

color("green")
right(55)
 
forward(20)
right(90)
forward(53)
right(90)
forward(50)
right(90)
forward(53)
right(90)
forward(30)

penup()
goto(130, 120)
pendown()
right(90)
forward(53)
right(90)
forward(53)
right(90)
forward(53)
right(90)
forward(53)
left(180)
forward(26)
left(90)
forward(53)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(53)
penup()
goto(40, 120)
pendown()
left(90)
forward(53)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(53)
penup()
goto(155, 250)
pendown()
right(90)
color("brown")
begin_fill()
forward(50)
right(90)
forward(20)
right(90)
forward(50)
right(90)
forward(20)
end_fill()
penup()
goto(130 ,50)
pendown()
forward(5)

exitonclick()
