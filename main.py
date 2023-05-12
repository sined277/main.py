import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create a screen object and set its attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('TURTLE CROSSING')

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up the screen event listener for player movement
screen.listen()
screen.onkey(player.up, 'w')

# Set up the game loop
game_is_on = True
while game_is_on:
    # Add a delay to the game loop
    time.sleep(0.1)

    # Update the screen
    screen.update()

    # Detect collision with a car
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            # End the game and display "Game Over" message
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        # Reset the player's position, increase the level, and update the scoreboard
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    # Move the cars, create new cars if necessary
    car_manager.move()
    car_manager.create_car()

# Exit the game when the user clicks on the screen
screen.exitonclick()
