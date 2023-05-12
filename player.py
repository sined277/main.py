from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.go_to_start()
        self.color('black')
        self.setheading(90)


    # Move the player turtle forward by MOVE_DISTANCE.
    def up(self):
        self.forward(MOVE_DISTANCE)

    # Check if the player turtle has reached the finish line.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    # Move the player turtle to the starting position.
    def go_to_start(self):
        self.goto(STARTING_POSITION)
