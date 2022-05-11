from turtle import Turtle

class Name(Turtle):

    def __init__(self, name):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.name = name
        #self.goto(x=0, y=0)
        self.speed("fastest")


    def correct_answer(self, x, y):
        self.goto(x=x, y=y)
        self.write(f"{self.name}", align="center", font=("Arial", 12, "normal"))