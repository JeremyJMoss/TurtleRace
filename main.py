from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a colour from this list.\nRed, Orange, "
                            "Yellow, Green, Blue and Purple:")

turtles = []
position_y = -100

for num in range(0, 6):
    turtle = Turtle("turtle")
    turtle.color(colors[num])
    turtles.append(turtle)
    turtles[num].penup()
    turtles[num].speed("slowest")
    turtles[num].goto(-225, position_y)
    position_y += 40

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")

