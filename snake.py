import turtle
import time
import random

#cons
wait = 0.1
score = 0
high_score = 0

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
figures = []

#texto
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup
text.hideturtle
text.goto(0,260)
text.write("Score: {}     High score: {}", align= "center".format(score, high_score), 
    font=("courier", 24, "normal"))

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
    
    #colisiones bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #esconder los segmentos
        for figure in figures:
            figure.goto(1000,1000)
        #limpiar lista de segmentos
        figures.clear()   

    #colisiones comida
    if head.distance(food) < 20:
        #mover cabeza
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        new_figure = turtle.Turtle()  
        new_figure.speed(0)
        new_figure.shape("square")
        new_figure.color("grey")
        new_figure.penup()
        figures.append(new_figure)

        #aumentar segmento
        score += 10

        if score > high_score:
            high_score = score
        
        text.write("Score: {}     High score: {}".format(score, high_score),
             align= "center", font=("courier", 24, "normal"))
    
    #mover el cuerpo de la serpiente
    total_figures = len(figures)
    for index in range(total_figures -1, 0, -1):
        x = figures[index -1].xcor() 
        y = figures[index -1].ycor()
        figures[index].goto(x,y)
    
    if total_figures > 0:
        x = head.xcor()
        y = head.ycor()
        figures[0].goto(x,y)
    #resetear segmentos/resetear marcador
        score = 0
        text.clear()
        text.write("Score: {}     High score: {}".format(score, high_score),
             align= "center", font=("courier", 24, "normal"))

    move()

    #colisiones con el cuerpo
    for figure in figures:
        if figure.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #esconder los segmentos
            for figure in figures:
                figure.goto(1000,1000)
            figures.clear()
    time.sleep(wait)
