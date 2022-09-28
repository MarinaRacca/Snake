import turtle
import time
import random

#cons
wait = 0.1

#ventana
snake = turtle.Screen()
snake.title("Juego snake")
snake.bgcolor("black")
snake.setup(width = 600, height = 600)
snake.tracer(0)

#cabeza serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "up"

#comida
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.penup("red")
food.goto(0,100)

#cuerpo serpiente

#funciones
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#teclado
snake.listen()
snake.onkeypress(up, "up")
snake.onkeypress(down, "down")
snake.onkeypress(left, "left")
snake.onkeypress(right, "right")

while True:
    snake.update()

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randit(-280,280)
        food.goto(x,y)
    move()
    time.sleep(wait)