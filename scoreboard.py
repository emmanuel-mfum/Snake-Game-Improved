from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:  # reading the highest score from the file
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.penup()
        self.hideturtle()

    def display(self):  # method to display the score
        self.clear()  # clears the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as f:
                f.write(f"{self.high_score}")

        self.score = 0  # resets the score
        self.display()

    def increase_score(self):  # method to increase the score
        self.score += 1   # increments score
        self.display()  # displays again the score
