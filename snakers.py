from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard


import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakers")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food.
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        score.reset()
        snake.reset()
    # Detect collision with tail.
    for block in snake.snake_blocks[1:]:
        if snake.snake_head.distance(block) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
