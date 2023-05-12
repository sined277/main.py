from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score_board()

    def update_score_board(self):
        # Clear the scoreboard and write the current level
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        # Increase the level and update the scoreboard
        self.level += 1
        self.update_score_board()

    def game_over(self):
        # Display "GAME OVER" in the center of the screen
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
