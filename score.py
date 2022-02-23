from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as data:
                self.high_score = data.write(str(self.score))
                data.close()
            with open("data.txt", mode="r") as data:
                self.high_score = data.read()


        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()










