from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")
GFONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as h_score:
            self.high_score = int(h_score.read())
        # self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, ALIGN, FONT)

    # def game_over(self):
    #     # self.clear()
    #     self.home()
    #     self.write("Game Over!", False, ALIGN, GFONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as store:
            store.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
