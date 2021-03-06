from turtle import Turtle

from winsound import PlaySound, SND_ASYNC
from global_helpers import get_random_color, get_random_location
from global_helpers import FOOD_COLORS


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(get_random_color(FOOD_COLORS))
        self.speed("fastest")

        self.goto(get_random_location())

    def move_food(self):
        """Moves the food to a new location and set's it to a random color"""
        self.goto(get_random_location())
        self.color(get_random_color(FOOD_COLORS))

    
    def change_color(self):
        """Updates the color of the food to a new random color from the list"""
        self.color(get_random_color(FOOD_COLORS))
    
    def update_food(self):
        """Does everything required to update the food"""
        self.move_food()
        self.change_color()
        PlaySound("./music/coin_collect.wav", SND_ASYNC)