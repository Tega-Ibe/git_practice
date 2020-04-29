import turtle

def draw_square(x, y):
    turtle.penup()
    turtle.setheading(0)
    turtle.setposition(x, y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(10)
        turtle.left(90)
    turtle.update()
    
turtle.tracer(0)
turtle.hideturtle()

turtle.onscreenclick(draw_square)


turtle.mainloop()