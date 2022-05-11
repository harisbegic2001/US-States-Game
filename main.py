#Required libraries
import turtle
from turtle import Turtle,Screen
import pandas
from Country_Name import Name

#Correct answer counter
corr_answ = 0

#Setting up the screen using Turtle
screen = Screen()
screen.setup(width=700, height=500)
screen.title("US STATES GAME")
screen.bgpic("blank_states_img.gif")

#Testing Turtle positions
#test_turtle = Turtle()
#test_turtle.shape("square")
#test_turtle.penup()
#test_turtle.goto(x=312, y=112)

#Using pandas for data reading
data = pandas.read_csv("50_states.csv")

list_of_countries = data["state"].tolist()

#print(list_of_countries)

#Gameplay
game_is_on = True
while game_is_on:
    # Input board settings
    board = turtle.textinput(f"{corr_answ}/50 States correct", prompt="What's another state name")

    if board in list_of_countries:
        new_country = Name(board)
        corr_answ += 1
        state_data = data[data["state"] == board]
        x_cor = int(state_data["x"])
        y_cor = int(state_data["y"])
        new_country.correct_answer(x=x_cor, y=y_cor)
        list_of_countries.remove(board)


    if corr_answ == 50:
        print("YOU WON THE GAME")
        game_is_on = False


















screen.exitonclick()
