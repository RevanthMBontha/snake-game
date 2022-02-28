import time
from turtle import Screen

from food import Food
from global_helpers import CONTACT_THRESHOLD, GAME_REFRESH_RATE
from scoreboard import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating a snake
snake = Snake()

# Creating food for the snake
food = Food()

# Creating the scoreboard
score_board = Score()

# Setting the screen to listen
screen.listen()

# Moving the snake on the screen
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)

# Running the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_REFRESH_RATE)

    snake.move()

    # Check Collision with food
    if snake.head.distance(food) < CONTACT_THRESHOLD:
        food.move_food()
        snake.extend_snake()
        score_board.update_score()

    # Check collision with wall
    if not (-290 <= snake.head.xcor() <= 290) or not (-290 <= snake.head.ycor() <= 290):
        game_is_on = False
        score_board.game_over()

    # Check collision with self
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) <= CONTACT_THRESHOLD:
            snake.is_alive = False
            score_board.game_over()
            game_is_on = False
            break

# Game Over functionality


screen.exitonclick()
