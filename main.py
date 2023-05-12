import  Jugada , Juego
from jugador import  Jugador, JugadorHumano , JugadorMaquina
jugador1= JugadorHumano("HHHHHHHHHHHHH")  #define el objeto jugador1 cuyo atributo es "nombre"
jugador2= JugadorMaquina()                #define el objeto jugador2 cuyo atributo es default en clase JugadorMaquina

juego = Juego.Juego(jugador1 , jugador2) #definir el objeto juego ,cuyos atributos son otros objetos de las clases JugadorHumano y JugadorMaquina 

juego.iniciar()      #llama a una función que no hace nada ?????????????????????? , pero extrañamente funciona
while not (jugador1.score == 5 or jugador2.score == 5):  #bucle while que termina cuando el primer jugador alcance 5 puntos
    
    valor1 = JugadorHumano.jugar(jugador1)  #llama a la función jugar de la clase JugadorHumano cuyo INPUT es el objeto jugador1 y output es valor1
                                            #valor1 es el RESULTADO de la llamada de la función jugar
                                            #POR AQUI ENTRA EL INPUT!!!!!!!!!!!!!
                                            #el input tiene que ser un objeto de la clase jugadorHumano 
                                            #(jugador1)==(self) , self es un objeto genérico de la clase y jugador1 es un objeto específico de la clase
                                            #valor1 es un OUTPUT .
    valor2= JugadorMaquina.jugar(jugador2)
    jugada1 = Jugada.Jugada(valor1 , valor2)

    resultado1 = Jugada.Jugada.func(jugada1)
    print(valor1)
    print(valor2)

    if resultado1 == True:
        jugador1.score += 1
        print("Has Ganado")
    else :
    
        if valor1 == valor2:
            print( "Empate")
        else:
            jugador2.score+=1
            print("Has perdido")
        
    print("Jugador Humano :  " , jugador1.score," - " ,"Jugador Maquina : " ,  jugador2.score )
if jugador2.score == 5:
    print( "Jugador Maquina ha ganado")
else:
    print("Jugador Humano ha ganado")