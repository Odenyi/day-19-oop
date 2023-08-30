import random
from turtle import Turtle,Screen

screen = Screen()
# set screen height and width
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","blue","purple"]
index =0
yaxis = -100
turtles = []
israceon = False

bet =screen.textinput(title="make you bet",prompt="which turtle will win the race?enter color")
for turtle_number in range(0, 6):

    new_turtle =Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])

    new_turtle.goto(-230, yaxis)

    # add turtle to
    turtles.append(new_turtle)
    yaxis +=40
    index +=1
if bet:
    israceon = True
while israceon:
    for turtle in turtles:
        if turtle.xcor()>230:
            israceon = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"you have won the winning color is {bet}")
            else:
                print(f"you have lost the winning color is {winning_color}")

        randomint = random.randint(0,10)
        turtle.forward(randomint)









# # hetcha sketcha
# def move_foward():
#     odenyi.forward(10)
# def move_backward():
#     odenyi.back(10)
# # def conterclockwise():
# #     odenyi.circle(5,odenyi.heading(),-20)
# # def clockwise():
# #     odenyi.circle(5,odenyi.heading(),20)
# def turnleft():
#
#     odenyi.left(45)
# def turnright():
#
#     odenyi.right(45)
# def clearscreen():
#     odenyi.clear()
#     odenyi.penup()
#     odenyi.home()
#     odenyi.pendown()
# screen.listen()
# screen.onkey(key="W", fun=move_foward)
# screen.onkey(key="S", fun=move_backward)
# screen.onkey(key="D", fun=turnleft)
# screen.onkey(key="A", fun=turnright)
# screen.onkey(key="C", fun=clearscreen)
screen.exitonclick()