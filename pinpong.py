import time
import turtle
import pygame
pygame.init()
from pygame import mixer
from pygame.locals import *

window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800,height=700)
window.tracer(0)

score_a = 0
score_b = 0


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=7,stretch_len=-1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-370,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=7,stretch_len=-1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(370,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=1,stretch_len=-1)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = -0.4

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player1: 0 Player2: 0", align="center", font=("courier",20))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 320:
        ball.sety(320)
        ball.dy *= -1
        bounce_sound = pygame.mixer.Sound("asound.wav")
        bounce_sound.play()

    if ball.ycor() < -320:
        ball.sety(-320)
        ball.dy *= -1
        bounce_sound = pygame.mixer.Sound("asound.wav")
        bounce_sound.play()

    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        bounce_sound = pygame.mixer.Sound("asound.wav")
        bounce_sound.play()
        pen.clear()
        pen.write("Player1: {} Player2: {}".format(score_a, score_b), align = "center", font = ("courier", 20))

    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        bounce_sound = pygame.mixer.Sound("asound.wav")
        bounce_sound.play()
        pen.clear()
        pen.write("Player1: {} Player2: {}".format(score_a, score_b), align = "center", font = ("courier", 20))

    if ball.xcor() > 360 and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() - 45):
        ball.dx *= -1
        bounce_sound = pygame.mixer.Sound("beep.wav")
        bounce_sound.play()

    if ball.xcor() < -360 and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() - 45):
        ball.dx *= -1
        bounce_sound = pygame.mixer.Sound("beep.wav")
        bounce_sound.play()