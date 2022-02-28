from winsound import PlaySound, SND_ASYNC
from turtle import Turtle

from global_helpers import FONT, ALIGNMENT


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 250)
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.show_score()

    def update_score(self):
        """Updates the score and displays the new score"""
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        """Displays the score"""
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=(FONT, 18, "normal"))

    def game_over(self):
        """Displays the messages when the game is over"""
        self.setpos(0, 0)
        self.color("tomato3")
        self.write(f"Game Over!", False, align=ALIGNMENT, font=(FONT, 30, "normal"))
        self.setpos(0, -15)
        self.write("Click to exit", False, align=ALIGNMENT, font=(FONT, 12, "normal"))
        PlaySound("./music/game_over.wav", SND_ASYNC)
