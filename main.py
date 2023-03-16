from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True
snake = Snake()
food = Food()
screen.listen()
screen.onkeypress(key="Up", fun=snake.turn_up)
screen.onkeypress(key="Right", fun=snake.turn_right)
screen.onkeypress(key="Left", fun=snake.turn_left)
screen.onkeypress(key="Down", fun=snake.turn_down)
scoreboard = ScoreBoard()


while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    if snake.head.distance(food) < 15:
        print("Yum.")
        food.go_to_random()
        snake.add_turtle()
        scoreboard.score += 1
        scoreboard.update()
    elif snake.head.xcor() == -320 or snake.head.xcor() == 320 or snake.head.ycor() == -220 or snake.head.ycor() == 220:
        scoreboard.game_over()
        game_is_on = False
    for turtle in snake.turtles[2:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
