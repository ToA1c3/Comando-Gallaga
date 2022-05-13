import turtle #Importacion de las librerias necesarias
import time
import random

player_dx=15
def move_l(): #Funcion para el movimiento a la  izq
    x=player.xcor()-player_dx
    if x<-190:
        x=-190
    player.setx(x)
    
def move_r(): #Funcion para movimiento a la derecha
    x=player.xcor()+player_dx
    if x>190:
        x=190
    player.setx(x)

def disparo(): #Funcion que efectua el disparo 
    x=player.xcor()
    y=player.ycor()
    bala.setposition(x,y+30)
    bala.showturtle()


#pantalla donde se desplegara el juego
ven=turtle.Screen()
ven.setup(width=540, height=540)
ven.bgcolor("lightblue")
ven.title("Comando Gallaga")

#borde de la pantalla donde apareceran el jugador, el proyectil y el enemigo
borde=turtle.Turtle()
borde.speed(0)
borde.color("black")
borde.up()
borde.setposition(-200,-200) #Limites
borde.down()
borde.pensize(4)
for side in range (4):
    borde.forward(400)
    borde.left(90)

borde.hideturtle()

#cuerpos
turtle.register_shape("gallina6.gif") #Player
turtle.register_shape("misil6.gif")   #Enemigo
turtle.register_shape("huevo4.gif")   #Proyectiles que lanza el jugador


#jugador/gallaga
player=turtle.Turtle()
player.shape("gallina6.gif") #Damos una imagen a el player
player.up()
player.speed(0)             #Velocidad inicial
player.setposition(0,-180)  #Posicion inicial
player.setheading(90)       #Angulo incial apuntando hacia arriba
player.shapesize(0.2,0.2)   #Tamaño de el player

#Puntuacion
score=0 

#marcador
score_m=turtle.Turtle()
score_m.speed(0)                     #Velocidad inicial
score_m.color("black")               #Color del marcador
score_m.up()               
score_m.setposition(-200,210)        #Posicion del marcador
score_m.write("Score: %s" %score)    #Desplegar el marcador
score_m.hideturtle()

#gusanos/armas
bala=turtle.Turtle()
bala.shape("huevo4.gif")  #Damos imagen a el proyectil
#bala.color("pink")
#bala.shape("square")
bala.up()
bala.speed(0)             #Velocidad incial 
bala.setheading(90)       #Angulo incial apntando hacia arriba
bala.shapesize(0.5,0.7)   #Tamaño del proyectil
bala.hideturtle()

#Misiles/enemigos
misil=turtle.Turtle()     
misil.shape("misil6.gif")    #Damos imagen a el enemigo
misil.up()
misil.speed(0)               #Velocidad inicial
misil.setposition(-180,180)  #Posicion inicial
misil.setheading(270)        #Angulo inicial apuntando hacia abajo

#teclado binds
turtle.listen()
turtle.onkey(move_l, "Left")  #Control para moverse a la izquierda
turtle.onkey(move_r, "Right") #Control para moverse a la derecha
turtle.onkey(disparo,"Up")    #Control para disparar

bala_speed=10   #Velocidad del proyectil
misil_speed=1   #Velocidad del misil
while True:     #Ciclo para registrar los impactos de el proyectil con el enemigo
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
        misil.setposition(x,180) #Reset de la posicion de el enemigo

        player.setposition(0,-180) #Reset del jugador