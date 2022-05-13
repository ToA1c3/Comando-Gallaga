import turtle
import time
import random

player_dx=15
def move_l():
    x=player.xcor()-player_dx
    if x<-190:
        x=-190
    player.setx(x)
    
def move_r():
    x=player.xcor()+player_dx
    if x>190:
        x=190
    player.setx(x)

def disparo():
    x=player.xcor()
    y=player.ycor()
    bala.setposition(x,y+30)
    bala.showturtle()


#pantalla
ven=turtle.Screen()
ven.setup(width=540, height=540)
ven.bgcolor("lightblue")
ven.title("Comando Gallaga")

#borde
borde=turtle.Turtle()
borde.speed(0)
borde.color("black")
borde.up()
borde.setposition(-200,-200)
borde.down()
borde.pensize(4)
for side in range (4):
    borde.forward(400)
    borde.left(90)

borde.hideturtle()

#cuerpos
turtle.register_shape("gallina6.gif")

#jugador/gallaga
player=turtle.Turtle()
player.shape("gallina6.gif")
#player.color("white")
#player.shape("square")
player.up()
player.speed(0)
player.setposition(0,-180)
player.setheading(90)
player.shapesize(0.2,0.2)

#Puntuacion
score=0

#marcador
score_m=turtle.Turtle()
score_m.speed(0)
score_m.color("black")
score_m.up()
score_m.setposition(-200,210)
score_m.write("Score: %s" %score)
score_m.hideturtle()

#gusanos/armas
bala=turtle.Turtle()
bala.color("pink")
bala.shape("square")
bala.up()
bala.speed(0)
bala.setheading(90)
bala.shapesize(0.5,0.7)
bala.hideturtle()

#Misiles/enemigos
misil=turtle.Turtle()
misil.shape("triangle")
misil.color("red")
misil.up()
misil.speed(0)
misil.setposition(-180,180)
misil.setheading(270)

#teclado binds
turtle.listen()
turtle.onkey(move_l, "Left")
turtle.onkey(move_r, "Right")
turtle.onkey(disparo,"Up")

bala_speed=10
misil_speed=3
while True:
    misil.forward(misil_speed)
    if misil.ycor() == -180:
        break
    bala.forward(bala_speed)
    if (-10 < (abs(bala.xcor()) - abs(misil.xcor())) < 10) and (-5 < (abs(bala.ycor()) - abs(misil.ycor())) < 5):
        
        #update score
        score=score+1
        score_m.clear()
        score_m.write("Score: %s" %score)

        bala.hideturtle()
        misil.hideturtle()
        time.sleep(2)

        misil.showturtle()
        x=random.randint(-180,180)
        misil.setposition(x,180)

        player.setposition(0,-180)

