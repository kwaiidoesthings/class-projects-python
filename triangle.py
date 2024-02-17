import turtle 

window = turtle.Screen()
turtle.fillcolor("black")
turtle.begin_fill
turtle.pendown()
triangle_a = int(input("Enter Angle A: "))
triangle_b = int(input("Enter Angle B: "))
triangle_c = int(input("Enter Angle C: "))

turtle.forward(300)
turtle.left(triangle_a)
turtle.forward(300)
turtle.left(triangle_b)
turtle.forward(300)
turtle.left(triangle_c)


window.exitonclick()