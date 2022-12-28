from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

# Snake Body
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("My Snake Game")

game_is_on = True
# screen.delay(5)
snake = Snake()
food = Food()
sb = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")


while game_is_on:
    # firse jayega
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.increase_score()
        snake.extend()

    # Collision to wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        sb.reset()
        snake.reset()

    # Collision with Tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            sb.reset()
            snake.reset()




# turtle ka dimensions= 20px * 20px hota hai







screen.exitonclick()