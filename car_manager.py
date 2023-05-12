from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []  # Creates an empty list to store the cars
        self.cars_speed = STARTING_MOVE_DISTANCE  # Initializes the cars' starting speed to 5 units


    def create_car(self):
        """
        Creates a new car and adds it to the car list randomly.
        """
        random_chance = random.randint(1, 6)  # Randomly generates a number between 1 and 6 (inclusive)
        if random_chance == 6:  # If the generated number is 6, create a new car
            new_car = Turtle('square')  # Creates a new Turtle object with a square shape
            new_car.turtlesize(stretch_wid=1, stretch_len=2)  # Resizes the turtle to make it look like a car
            new_car.penup()  # Lifts the pen up to avoid drawing lines while moving
            new_car.color(random.choice(COLORS))  # Assigns a random color to the new car
            random_y = random.randint(-250, 250)  # Generates a random y-coordinate between -250 and 250 (inclusive)
            new_car.goto(300, random_y)  # Positions the new car at the right edge of the screen with a random y-coordinate
            new_car.setheading(180)  # Makes the car face left
            self.car_list.append(new_car)  # Adds the new car to the car list


    def move(self):
        """
        Moves each car in the car list to the left by their respective speeds.
        """
        for car in self.car_list:
            car.forward(self.cars_speed)  # Moves the car to the left by its speed


    def level_up(self):
        """
        Increases the speed of the cars.
        """
        self.cars_speed += MOVE_INCREMENT  # Increases the cars' speed by 10 units
