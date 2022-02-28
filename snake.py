from turtle import Turtle

from global_helpers import MOVE_DISTANCE, UP, DOWN, LEFT, RIGHT
from global_helpers import STARTING_POSITIONS, SNAKE_COLORS, CONTACT_THRESHOLD, SNAKE_COMPRESS_RATIO
from global_helpers import get_random_color


class Snake:

    def __init__(self):
        self.is_alive = True
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the starting snake"""
        color = get_random_color(SNAKE_COLORS)
        for position in STARTING_POSITIONS:
            self.add_segment(position, color)

    def add_segment(self, _position, _color):
        """Adds a new segment to the snake"""
        new_segment = Turtle("square")
        new_segment.color(_color)
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.shapesize(stretch_wid=SNAKE_COMPRESS_RATIO, stretch_len=SNAKE_COMPRESS_RATIO)
        new_segment.goto(_position)
        self.segments.append(new_segment)

    def extend_snake(self):
        """Used to extend the length of the snake every time it eats food"""
        self.add_segment(self.segments[-1].pos(), self.head.pencolor())

    def move(self):
        """Keeps the snake moving while it is alive"""
        if self.is_alive:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                self.segments[seg_num].goto(self.segments[seg_num - 1].pos())

            self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """Set heading to UP"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """Set heading to DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """Set heading to LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """Set heading to RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


